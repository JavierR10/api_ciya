from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Máximo número de resultados por página

    def get_page_size(self, request):
        # Obtenemos el tamaño de página especificado en la solicitud, si está presente
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size and page_size.isdigit():
            return int(page_size)
        return self.page_size  # Si no se especifica, usamos el tamaño predeterminado

    def paginate_queryset(self, queryset, request, view=None):
        # Sobrescribimos este método para obtener el tamaño de página personalizado
        self.page_size = self.get_page_size(request)
        return super().paginate_queryset(queryset, request, view)
