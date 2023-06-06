from paddlenlp.utils.doc_parser import DocParser

doc_parser = DocParser(ocr_lang="ch")
doc_path = "/root/autodl-tmp/resume_parse/code/1.png"
parsed_doc = doc_parser.parse({"doc": doc_path})
doc_parser.write_image_with_results(
        doc_path,
        layout=parsed_doc['layout'],
        save_path="ocr_result.png")