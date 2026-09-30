from django.forms import ModelForm, TextInput, NumberInput, URLInput, Textarea
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
from main.models import Education, Experience

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "score",
            "category",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Lembaga",
            "score": "Nilai Akhir",
            "category": "Jenis Pendidikan",
            "started_at": "Tahun Mulai",
            "ended_at": "Tahun Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "SMAN 67 Indonesia",
                    "maxlength": 255,
                }
            ),
            "score": NumberInput(
                attrs={
                    "placeholder": "67.67",
                    "min": 0,
                    "max": 100,
                    "step": 0.01,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "informal / formal",
                }
            ),
            "started_at": NumberInput(
                attrs={
                    "placeholder": "2001",
                    "min": 1970,
                    "step": 1,
                }
            ),
            "ended_at": NumberInput(
                attrs={
                    "placeholder": "2067",
                    "min": 1970,
                    "step": 1,
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data.get("title", "")).strip()
        if not title:
            raise ValidationError("Nama lembaga tidak boleh hanya berisi tag HTML.")
        return title

    def clean_category(self):
        return strip_tags(self.cleaned_data.get("category", "")).strip()

    def clean(self):
        cleaned_data = super().clean()
        started_at = cleaned_data.get("started_at")
        ended_at = cleaned_data.get("ended_at")

        if started_at and ended_at and ended_at < started_at:
            self.add_error(
                "ended_at",
                "Tahun selesai tidak bisa lebih dulu dari tahun mulai"
            )

        return cleaned_data


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Jenis Pengalaman",
            "thumbnail": "URL Thumbnail",
            "started_at": "Tahun Mulai",
            "ended_at": "Tahun Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi pengalaman...",
                    "rows": 4,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "internship / research / volunteer / part-time / full-time / freelance",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
            "started_at": NumberInput(
                attrs={
                    "placeholder": "2024",
                    "min": 1970,
                    "step": 1,
                }
            ),
            "ended_at": NumberInput(
                attrs={
                    "placeholder": "2026 (kosongkan jika masih berlangsung)",
                    "min": 1970,
                    "step": 1,
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data.get("title", "")).strip()
        if not title:
            raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data.get("description", "")).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data.get("category", "")).strip()

    def clean(self):
        cleaned_data = super().clean()
        started_at = cleaned_data.get("started_at")
        ended_at = cleaned_data.get("ended_at")

        if started_at and ended_at and ended_at < started_at:
            self.add_error(
                "ended_at",
                "Tahun selesai tidak bisa lebih dulu dari tahun mulai"
            )

        return cleaned_data
