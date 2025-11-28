from django.db import models

class Posts(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    post_author = models.BigIntegerField(null=True)
    post_date = models.DateTimeField(null=True)
    post_date_gmt = models.DateTimeField(null=True)
    post_content = models.TextField(null=True)
    post_title = models.TextField(max_length=300)
    post_excerpt = models.TextField(null=True)
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20, null=True)
    ping_status = models.CharField(max_length=20, null=True)
    post_password = models.CharField(max_length=255, null=True)
    post_name = models.CharField(max_length=200, null=True)
    to_ping = models.TextField(null=True)
    pinged = models.TextField(null=True)
    post_modified = models.DateTimeField(null=True)
    post_modified_gmt = models.DateTimeField(null=True)
    post_content_filtered = models.TextField(null=True)
    post_parent = models.BigIntegerField(null=True)
    guid = models.TextField(null=True)
    menu_order = models.IntegerField(null=True)
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100, null=True)
    comment_count = models.IntegerField(null=True)

    class Meta:
        db_table = 'wpsv_posts'
        managed = False

class ProductMetaLookup(models.Model):
    product = models.OneToOneField(
        Posts,
        on_delete=models.CASCADE,
        db_column='product_id',
        primary_key=True,
        related_name='meta'
    )

    sku = models.CharField(max_length=255, null=True)
    global_unique_id = models.CharField(max_length=255, null=True)
    virtual = models.BooleanField(null=True)
    downloadable = models.BooleanField(null=True)

    min_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    max_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    onsale = models.BooleanField(null=True)

    stock_quantity = models.IntegerField(null=True)
    stock_status = models.CharField(max_length=20, null=True)

    rating_count = models.IntegerField(null=True)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    total_sales = models.IntegerField(null=True)

    tax_status = models.CharField(max_length=20, null=True)
    tax_class = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'wpsv_wc_product_meta_lookup'
        managed = False

class PostMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)

    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        db_column='post_id',
        related_name='meta_values'
    )

    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField(null=True)

    class Meta:
        db_table = 'wpsv_postmeta'
        managed = False
