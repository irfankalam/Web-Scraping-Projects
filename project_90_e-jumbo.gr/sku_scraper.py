# coding: utf-8

from bs4 import BeautifulSoup
import json
import csv
import time
import re
import requests

def sku_scrape(data_parent_id,data_path,skuId):
    headers_0 = {
        'authority': 'www.e-jumbo.gr',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.e-jumbo.gr',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.e-jumbo.gr/vrefika-eidi/vrefanaptyxi/peripoiisi-stithous-miteras/esoroucha-egkymosynis/soutien-egkymosynis-nude-lefki-dantela_1445696/?country=GR',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    params_0 = (
        ('lang', 'el'),
        ('country', 'cy'),
    )


    data_0 = {}

    d_value_data = "{\"__type\":\"Lighthouse.Lh3.FrontEnd.Root.Model.AdapterParameters, Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"LoaderOptions\":{\"__type\":\"Lighthouse.Lh3.FrontEnd.Controls.Builtin.ProductDetailsLoaderOptions, Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"ParentProductId\":1445696,\"PathChecksum\":526038316,\"LanguageId\":1,\"SkuId\":1388210,\"SplitDimensions\":null,\"BundleItems\":[],\"ItemAttributes\":[],\"LanguageCode\":\"el\",\"CurrencyCode\":\"EUR\",\"SiteCode\":\"www-e-jumbo-gr\",\"Cacher\":null},\"AdapterOptions\":{\"__type\":\"Lighthouse.Lh3.FrontEnd.Root.Model.ProductDetailsBaseAdapter+ProductDetailsAdapterParams, Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"IsDynamic\":false,\"EnableNoImage\":true,\"DimensionImageTypes\":[],\"SelectDefaultSku\":false,\"Actions\":2147483647,\"LazyLoadPrices\":false,\"AttributesStartIndex\":null,\"Articles\":{},\"Literals\":{\"QuantityText\":\"ΠΟΣΟΤΗΤΑ:\",\"VatText\":\"Στην τιμή συμπεριλαμβάνεται ο Φ.Π.A.\",\"ShopOnlyProductBtnText\":\"ΕΠΙΚΟΙΝΩΝΗΣΤΕ ΜΕ ΚΑΤΑΣΤΗΜΑ\",\"ShopOnlyProductBtnText2\":\"βρες το πλησιέστερο\",\"StoresLocatorUrl\":\"http://corporate.e-jumbo.gr/katastimata-jumbo/\",\"ShopOnlyProductBtnTextUrl\":\"εδώ\",\"IsBatteryRequiredText\":\"ΛΕΙΤΟΥΡΓΕΙ ΜΕ ΜΠΑΤΑΡΙΕΣ\",\"BatteryBuyText\":\"ΔΕΙΤΕ ΕΔΩ\",\"IsBatteryRequiredUrl\":\"/paichnidia/bataries-alkalikes/\",\"SafeProductTitle\":\"ΚΑΤΑΛΛΗΛΟΤΗΤΑ ΠΡΟΪΟΝΤΟΣ\",\"PriceText\":\"ΤΙΜΗ JUMBO:\",\"AvailabilityText\":\"Διαθεσιμότητα:\",\"OrderedWithIconClass\":\"rocket\",\"GalleryText\":\"Τοποθετήστε τον κέρσορα στη φωτογραφία για μεγέθυνση\",\"AssortmentCodesText\":\"Το προϊόν είναι κωδικός τυχαίας επιλογής, δηλαδή διατίθεται σε παραπάνω από ένα σχέδια ή χρώματα. Δείτε τους όρους και προϋποθέσεις επιστροφών κωδικών τυχαίας επιλογής.\",\"DescriptionTabTitle\":\"Video\",\"VideoThumb\":\"VIDEO\",\"SafeClothingTitle\":\"ΠΙΣΤΟΠΟΙΗΣΗ\",\"SafeClothingTooltip\":\"Έχει ελεγχθεί για βλαβερές ουσίες\",\"SafeDishwasherTooltip\":\"Το προϊόν <span>δεν</span> είναι κατάλληλο για πλυντήριο πιάτων\",\"SafeMicrowaveTooltip\":\"Το προϊόν <span>δεν</span> είναι κατάλληλο για φούρνο μικροκυμάτων\",\"SuitableTitle\":\"ΚΑΤΑΛΛΗΛΟΤΗΤΑ\",\"WarehouseTooltip\":\"Επιλέξτε πρώτα μέγεθος για να δείτε την διαθεσιμότητα στα καταστήματα\",\"AvailabilityLabel\":\"Επιλέξτε μέγεθος για να δείτε την διαθεσιμότητα\",\"TabOneLabel\":\"Περιγραφή\",\"TabTwoLabel\":\"Μεταφορικά Έξοδα\",\"TabThreeLabel\":\"Επιστροφές\",\"TabFourLabel\":\"Χρόνοι Παράδοσης\",\"SizeGuideLabel\":\"Βρες το μέγεθος σου εδώ\",\"CanonicalLabel\":\"Δείτε τα όλα εδώ\",\"InstructionsPdfTitle\":\"Οδηγίες χρήσεως-συναρμολόγησης \",\"InstructionsPdfUrl\":\"Λήψη αρχείου PDF\"},\"SocialShares\":null,\"ProductReview\":null,\"WarehouseAvailabilities\":{\"__type\":\"Lighthouse.Lh3.FrontEnd.Root.Model.ProductWarehouseAvailabilityDataViewModel, Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"GeoLocationWithZipCode\":true,\"IgnoreAvailability\":true,\"WarehouseResultsCount\":100000,\"PartnerGroupBy\":\"\",\"SelectStores\":false,\"EnableTrackingLocation\":false,\"WarehouseDistances\":[{\"__type\":\"Lighthouse.Lh3.FrontEnd.Root.Model.DistanceSetValueOptions, Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"Value\":\"1000000\",\"Name\":\"χωρίς όριο\"}],\"CheckAvailabilityText\":\"ΑΝΑΖΗΤΗΣΗ ΚΑΤΑΣΤΗΜΑΤΩΝ\",\"CheckAvailabilityWithTrackingLocationText\":\"Search Warehouses Near My Location\",\"ShowWarehouseSearchText\":\"ΕΛΕΓΧΟΣ ΔΙΑΘΕΣΙΜΟΤΗΤΑΣ ΣΤΑ ΚΑΤΑΣΤΗΜΑΤΑ\",\"WarehouseHelpText\":\"Εισάγετε τον ΤΚ σας και δείτε τη διαθεσιμότητα στα καταστήματα Jumbo που βρίσκονται δίπλα σας.\",\"WarehouseHelpTextTwo\":\"Ελέγξτε την διαθεσιμότητα του προϊόντος στο κατάστημα της επιλογής σας:\",\"WarehouseTitle\":\"Διαθεσιμότητα σε κατάστημα\",\"WarehouseSearchText\":\"Εισάγετε ΤΚ\",\"WarehouseDistancesText\":\"Μέγιστη απόσταση\",\"WarehouseContinueShopping\":\"SELECT STORE & CONTINUE SHOPPING\",\"WarehouseProceedToCheckout\":\"SELECT STORE & PROCEED TO CHECKOUT\",\"LocationText\":\"Εισάγετε ΤΚ\",\"ErrorCalculatingDistancesText\":\"No calculation returned\",\"Configuration\":null,\"DebugInformation\":null}},\"LoaderAssemblyName\":\"Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"LoaderClassName\":\"Lighthouse.Lh3.FrontEnd.Controls.Builtin.ProductDetailsLoader\",\"AdapterAssemblyName\":\"Vendd.Website.Backend, Version=2020.4.0.72, Culture=neutral, PublicKeyToken=null\",\"AdapterClassName\":\"Lighthouse.Lh3.FrontEnd.Root.Model.ProductDetailsAdapter\"}"
    d_value = json.loads(d_value_data)
    d_value["LoaderOptions"]["ParentProductId"] = int(data_parent_id)
    d_value["LoaderOptions"]["PathChecksum"] = int(data_path)
    d_value["LoaderOptions"]["SkuId"] = int(skuId)
    d_value = json.dumps(d_value)

    data_0["serviceConfiguration"] = d_value
    data_0 = json.dumps(data_0)
    r_0 = requests.post('https://www.e-jumbo.gr/services/AdapterService.svc/GetData', headers=headers_0, params=params_0, data=data_0)

    s_data_raw = r_0.json()
    s_data = json.loads(s_data_raw["d"])
    s_sku = str(s_data["SkuCode"]).strip()
    return(s_sku)
