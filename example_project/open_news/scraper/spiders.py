from __future__ import unicode_literals
from dynamic_scraper.spiders.django_spider import DjangoSpider
from cdiscount.models import CDiscountWebsite, ProduitSolde, ProduitSoldeItem
import logging


class ProduitSoldeSpider(DjangoSpider):
    name = 'produit_solde_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(CDiscountWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        if len(self.ref_object.allowed_domain) > 0:
            self.log('Set Allowed Domaine : %s ' % self.ref_object.allowed_domain, logging.INFO)
            self.allowed_domains.append(self.ref_object.allowed_domain)
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = ProduitSolde
        self.scraped_obj_item_class = ProduitSoldeItem
        super(ProduitSoldeSpider, self).__init__(self, *args, **kwargs)
