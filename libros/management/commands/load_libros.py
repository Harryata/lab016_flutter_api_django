import json
from django.core.management.base import BaseCommand
from libros.models import Libro
from pathlib import Path

class Command(BaseCommand):
    help = 'Carga libros desde un archivo JSON'

    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent
        json_path = base_dir / 'data' / 'libros.json'

        with open(json_path, 'r', encoding='utf-8') as file:
            libros = json.load(file)

        for item in libros:
            Libro.objects.get_or_create(
                isbn=item['isbn'],
                defaults={
                    'titulo': item['titulo'],
                    'autor': item['autor'],
                    'fecha_publicacion': item['fecha_publicacion']
                }
            )

        self.stdout.write(self.style.SUCCESS('Libros cargados correctamente'))
