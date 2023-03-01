from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-mail', max_length=100)
    phone_number = models.CharField('Telefone', unique=True, null=False, blank=False, max_length=11)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['name']

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField('Produto', max_length=20, default='')
    user_id = models.ForeignKey("core.User", verbose_name="Usuario", on_delete=models.CASCADE)
    item_description = models.TextField('Descrição', max_length=200)
    item_quantity = models.IntegerField('Quantidade')
    item_price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    total_value = models.DecimalField('Total', decimal_places=2, max_digits=65, blank=True, null=True)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['item']
    
    def save(self):
        self.total_value = self.item_price * self.item_quantity
        super().save()

    def __str__(self):
        return self.item
    