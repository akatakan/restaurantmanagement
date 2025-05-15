from enum import Enum


class SiparisDurumu(Enum):
    ALINDI = "Alındı"
    HAZIRLANIYOR = "Hazırlanıyor"
    HAZIR = "Hazır"
    SERVIS_EDILDI = "Servis edildi"
    ODENDI = "Ödendi"
    IPTAL = "Iptal Edildi"
