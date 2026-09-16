from django.forms import ModelForm, TextInput, NumberInput
from main.models import Education

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
