import os
import argparse
import tqdm
import fitz  # PyMuPDF
from paddleocr import PaddleOCR


def extract_pdf_with_ocr(pdf_path, out_dir, verbose=True):
    """从PDF文件中提取文本和图片，并对图片进行OCR识别
    
    Args:
        pdf_path (str): PDF文件路径
        out_dir (str): 输出目录
        verbose (bool): 是否显示详细信息
    """
    # 参数验证
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")
    
    # 创建输出目录
    os.makedirs(out_dir, exist_ok=True)
    assets_dir = os.path.join(out_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    # 初始化OCR（中文+英文）
    if verbose:
        print("正在初始化OCR引擎...")
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    
    try:
        doc = fitz.open(pdf_path)
        pdf_basename = os.path.splitext(os.path.basename(pdf_path))[0]
        md_path = os.path.join(out_dir, pdf_basename + ".md")
        
        with open(md_path, "w", encoding="utf-8") as out:
            out.write(f"# {pdf_basename}\n\n")
            
            # 使用tqdm添加进度条 - 修复为tqdm.tqdm()
            with tqdm.tqdm(total=len(doc), desc="处理进度", unit="页") as pbar:
                for page_num in range(len(doc)):
                    page = doc[page_num]
                    page_actual_num = page_num + 1
                    
                    out.write(f"\n---\n\n## Page {page_actual_num}\n\n")
                    blocks = page.get_text("blocks")  # 按坐标提取文字块
                    blocks = sorted(blocks, key=lambda b: (b[1], b[0]))  # 按y、x排序
                    
                    # 标记是否找到了图片块
                    has_image_blocks = False
                    
                    for b in blocks:
                        if b[6] == 0:  # 文本块
                            text = b[4].strip()
                            if text:
                                out.write(text + "\n\n")
                        elif b[6] == 1:  # 图片块
                            has_image_blocks = True
                            xref = b[7]
                            try:
                                # 处理图片
                                pix = fitz.Pixmap(doc, xref)
                                try:
                                    if pix.n > 4:  # 确保是RGB模式
                                        pix = fitz.Pixmap(fitz.csRGB, pix)
                                    
                                    img_name = f"p{page_actual_num}_{xref}.png"
                                    img_path = os.path.join(assets_dir, img_name)
                                    pix.save(img_path)
                                    
                                    out.write(f"![{img_name}](assets/{img_name})\n\n")
                                    
                                    # OCR 识别图片
                                    try:
                                        ocr_result = ocr.ocr(img_path, cls=True)
                                        if ocr_result and len(ocr_result) > 0 and ocr_result[0]:
                                            ocr_texts = [line[1][0] for line in ocr_result[0]]
                                            if ocr_texts:
                                                out.write("**OCR识别内容：**\n\n")
                                                out.write("> " + "\n> ".join(ocr_texts) + "\n\n")
                                    except Exception as e:
                                        if verbose:
                                            print(f"页面{page_actual_num}图片OCR识别失败: {str(e)}")
                                finally:
                                    # 释放图片资源
                                    pix = None
                            except Exception as e:
                                if verbose:
                                    print(f"页面{page_actual_num}图片处理失败: {str(e)}")
                    
                    # 如果没有找到图片块，将整个页面渲染为图片（处理矢量图流程图）
                    if not has_image_blocks:
                        if verbose:
                            print(f"页面{page_actual_num}未找到图片块，尝试将整个页面渲染为图片...")
                        
                        # 设置高分辨率渲染参数
                        zoom = 3.0  # 缩放因子，值越大分辨率越高
                        matrix = fitz.Matrix(zoom, zoom)
                        
                        # 渲染整个页面为图片
                        try:
                            pix = page.get_pixmap(matrix=matrix)
                            
                            # 保存渲染的页面图片
                            img_name = f"page_{page_actual_num}_rendered.png"
                            img_path = os.path.join(assets_dir, img_name)
                            pix.save(img_path)
                            
                            out.write(f"![渲染页面](assets/{img_name})\n\n")
                            
                            # OCR 识别渲染的页面图片
                            try:
                                ocr_result = ocr.ocr(img_path, cls=True)
                                if ocr_result and len(ocr_result) > 0 and ocr_result[0]:
                                    ocr_texts = [line[1][0] for line in ocr_result[0]]
                                    if ocr_texts:
                                        out.write("**OCR页面识别内容：**\n\n")
                                        out.write("> " + "\n> ".join(ocr_texts) + "\n\n")
                            except Exception as e:
                                if verbose:
                                    print(f"页面{page_actual_num}渲染图片OCR识别失败: {str(e)}")
                        except Exception as e:
                            if verbose:
                                print(f"页面{page_actual_num}渲染失败: {str(e)}")
                        finally:
                            # 释放资源
                            pix = None
                    
                    pbar.update(1)  # 更新进度条
        
        if verbose:
            print(f"\n提取完成：{md_path}")
            print(f"图片保存目录：{assets_dir}")
    
    except Exception as e:
        print(f"处理PDF时出错: {str(e)}")
        raise
    finally:
        # 确保文档被正确关闭
        if 'doc' in locals() and doc is not None:
            doc.close()


def main():
    """主函数，处理命令行参数"""
    parser = argparse.ArgumentParser(description="PDF文本和图片提取工具，支持OCR识别")
    parser.add_argument("--pdf", required=True, help="PDF文件路径")
    parser.add_argument("--out", default="pdf_output", help="输出目录（默认：pdf_output）")
    parser.add_argument("--quiet", action="store_true", help="安静模式，不显示详细信息")
    
    args = parser.parse_args()
    extract_pdf_with_ocr(args.pdf, args.out, verbose=not args.quiet)


if __name__ == "__main__":
    try:
        # 尝试导入必要的依赖包，如果没有则安装
        import tqdm
        import fitz
        from paddleocr import PaddleOCR
    except ImportError as e:
        print(f"正在安装必要的依赖包: {str(e)}")
        os.system("pip install tqdm PyMuPDF paddleocr")
        
    # 如果直接运行脚本而不提供命令行参数，则使用示例
    import sys
    if len(sys.argv) == 1:
        pdf_path = "你的文件.pdf"
        print(f"使用示例模式：处理文件 '{pdf_path}'")
        print("提示：您可以使用命令行参数指定PDF文件路径和输出目录，例如:")
        print("python pdf_ocr.py --pdf your_file.pdf --out output_dir")
        # 由于没有实际文件，这里不执行实际处理，避免报错
        print("注意：请使用正确的PDF文件路径运行程序")
    else:
        main()