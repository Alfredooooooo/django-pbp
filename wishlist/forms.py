# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from wishlist.models import BarangWishlist


class BarangWishlistForm(ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ("nama_barang", "harga_barang", "deskripsi")

        labels = {
            "Nama Barang": "",
            "Harga Barang": "",
            "Deskripsi": "",
        }

        widgets = {
            "Nama Barang": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nama Barang mu"}),
            "Harga Barang": forms.TextInput(attrs={"class": "form-control", "placeholder": "Harganya Berapa"}),
            "Deskripsi": forms.TextInput(attrs={"class": "form-control", "placeholder": "Deskripsi"}),

        }
