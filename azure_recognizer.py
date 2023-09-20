from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential


class AzureRecognizer:
    def __init__(self, connection_key: str, connection_endpoint: str):
        self._document_analysis: DocumentAnalysisClient = self._authenticate(connection_endpoint, connection_key)
 
    def _authenticate(self, connection_endpoint: str, connection_key: str) -> None:
        return DocumentAnalysisClient(connection_endpoint, AzureKeyCredential(connection_key))

    def _format_key_value(self, result):
        fields_result = {}
        for kv_pair in result.key_value_pairs:
            if kv_pair.key:
                fields_result[kv_pair.key.content] = kv_pair.value.content if kv_pair.value else None
        return fields_result
    
    def process_file_content(self, path_pdf: str, service_read: str = "prebuilt-document", return_format: str = "key-value", page: int = None):
        with open(path_pdf, "rb") as fd:
            document = fd.read()

        azure_connection = self._document_analysis.begin_analyze_document(service_read, document, pages=page)
        result = azure_connection.result()

        if return_format == "key-value":
            return self._format_key_value(result)
        elif return_format == "text":
            return result.content
        else:
            raise Exception("Por el momento, no hay otro formato válido para devolver el contenido del pdf")