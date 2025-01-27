# from decimal import Decimal
# from django.db import models
# from customer.models import Customer, WholesaleCustomer, TransactionHistory
# from datetime import datetime
# from shortuuid.django_fields import ShortUUIDField


# # Create your models here.

# DOSAGE_FORM = [
#     ('Tablet', 'Tablet'),
#     ('Capsule', 'Capsule'),
#     ('Cream', 'Cream'),
#     ('Consumable', 'Consumable'),
#     ('Injection', 'Injection'),
#     ('Infusion', 'Infusion'),
#     ('Inhaler', 'Inhaler'),
#     ('Suspension', 'Suspension'),
#     ('Syrup', 'Syrup'),
#     ('Eye-drop', 'Eye-drop'),
#     ('Ear-drop', 'Ear-drop'),
#     ('Eye-ointment', 'Eye-ointment'),
#     ('Rectal', 'Rectal'),
#     ('Vaginal', 'Vaginal'),
# ]


# UNIT = [
#     ('Amp', 'Amp'),
#     ('Bottle', 'Bottle'),
#     ('Tab', 'Tab'),
#     ('Tin', 'Tin'),
#     ('Caps', 'Caps'),
#     ('Card', 'Card'),
#     ('Carton', 'Carton'),
#     ('Pack', 'Pack'),
#     ('Pcs', 'Pcs'),
#     ('Roll', 'Roll'),
#     ('Vail', 'Vail'),
#     ('1L', '1L'),
#     ('2L', '2L'),
#     ('4L', '4L'),
# ]

# MARKUP_CHOICES = [
#         (0, 'No markup'),
#         (2.5, '2.5% markup'),
#         (5, '5% markup'),
#         (7.5, '7.5% markup'),
#         (10, '10% markup'),
#         (12.5, '12.5% markup'),
#         (15, '15% markup'),
#         (17.5, '17.5% markup'),
#         (20, '20% markup'),
#         (22.5, '22.5% markup'),
#         (25, '25% markup'),
#         (27.5, '27.5% markup'),
#         (30, '30% markup'),
#         (32.5, '32.5% markup'),
#         (35, '35% markup'),
#         (37.5, '37.5% markup'),
#         (40, '40% markup'),
#         (42.5, '42.5% markup'),
#         (45, '45% markup'),
#         (47.5, '47.5% markup'),
#         (50, '50% markup'),
#         (57.5, '57.5% markup'),
#         (60, '60% markup'),
#         (62.5, '62.5% markup'),
#         (65, '65% markup'),
#         (67.5, '67.5% markup'),
#         (70, '70% markup'),
#         (72., '72.% markup'),
#         (75, '75% markup'),
#         (77.5, '77.5% markup'),
#         (80, '80% markup'),
#         (82.5, '82.% markup'),
#         (85, '85% markup'),
#         (87.5, '87.5% markup'),
#         (90, '90% markup'),
#         (92., '92.% markup'),
#         (95, '95% markup'),
#         (97.5, '97.5% markup'),
#         (100, '100% markup'),
#     ]


# STATUS_CHOICES = [
#         ('Returned', 'Returned'),
#         ('Partially Returned', 'Partially Returned'),
#         ('Dispensed', 'Dispensed'),
#     ]


# class Formulation(models.Model):
#     dosage_form = models.CharField(max_length=200, choices=DOSAGE_FORM, null=True, blank=True, default='DosageForm')
    
#     def __str__(self):
#         return self.dosage_form



# class WholesaleItem(models.Model):
#     name = models.CharField(max_length=200)
#     dosage_form = models.CharField(max_length=200, choices=DOSAGE_FORM, blank=True, null=True)
#     brand = models.CharField(max_length=200, blank=True, null=True)
#     unit = models.CharField(max_length=200, choices=UNIT, blank=True, null=True)
#     cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     markup = models.DecimalField(max_digits=6, decimal_places=2, default=0, choices=MARKUP_CHOICES)
#     stock = models.PositiveIntegerField(default=0, null=True, blank=True)
#     exp_date = models.DateField()    
    
#     class Meta:
#         ordering = ('name',)
    
#     def __str__(self):
#         return f'{self.name} {self.brand} {self.unit} {self.cost} {self.price} {self.markup} {self.stock} {self.exp_date}'
    
#     def save(self, *args, **kwargs):
#         # Check if the price was provided; if not, calculate based on the markup
#         if not self.price or self.price == self.cost + (self.cost * self.markup / 100):
#             self.price = self.cost + (self.cost * self.markup / 100)
#         super().save(*args, **kwargs)
