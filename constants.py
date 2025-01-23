import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

END_FILE_PREFIX = "revised_"
AI_NAME = "SyntAI"
DEFAULT_MODEL = "llama3.2:3b-instruct-q5_K_M"

SYNTAX_PROMPT = """
You are a proofreader specialist with the goal of pointing out syntax mistakes in your given assignment. You must only answer with either the phrase "This syntax is correct" or with "Here is what should be changed". When corrections are needed, you must give the before and after of the sentence that needs correcting. Make sure you read your assignments twice before answering, some are tricky.

Here is your assignment:
{}
"""

# Source of this: https://github.com/python-openxml/python-docx/issues/93
COMMENTS_PART_DEFAULT_XML_BYTES = (
    b"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r
<w:comments
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    xmlns:o="urn:schemas-microsoft-com:office:office"
    xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
    xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
    xmlns:w10="urn:schemas-microsoft-com:office:word"
    xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
    xmlns:sl="http://schemas.openxmlformats.org/schemaLibrary/2006/main"
    xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
    xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"
    xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"
    xmlns:lc="http://schemas.openxmlformats.org/drawingml/2006/lockedCanvas"
    xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram"
    xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
    xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
    xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
    xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml"
    xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml"
    xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex"
    xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid"
    xmlns:cr="http://schemas.microsoft.com/office/comments/2020/reactions">
</w:comments>
"""
).strip()


