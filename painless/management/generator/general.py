import os
import random
import secrets

from django.contrib.auth import get_user_model

from faker import Faker
from django.contrib.gis.geos import Point

from cms.submodels.banner import Banner
from cms.submodels.contact import Contact
from cms.submodels.faq import Faq
from cms.submodels.service import Service
from cms.submodels.setting import Setting
from cms.submodels.slider import Slider
from cms.submodels.social import Social

from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from product.submodels.attribute import Attribute, Data
from product.submodels.brand import Brand
from product.submodels.category import Category
from product.submodels.feature import Feature
from product.submodels.gallery import Gallery
from product.submodels.product import Product
from product.submodels.tag import Tag

fake = Faker()
fake_fa = Faker(['fa_IR'])


class CmsDataGenerator:
    def __init__(self):
        self.__social_name = ['facebook', 'instagram', 'whatsapp', 'twitter', 'telegram']

        self.__service_data = [
            {'svg': "media/static/web/assets/img/svg/delivery.svg", 'name': "تحویل اکسپرس"},
            {'svg': "media/static/web/assets/img/svg/contact-us.svg", 'name': "پشتیبانی 24 ساعته"},
            {'svg': "media/static/web/assets/img/svg/payment-terms.svg", 'name': "پرداخت درمحل"},
            {'svg': "media/static/web/assets/img/svg/return-policy.svg", 'name': "۷ روز ضمانت بازگشت"},
            {'svg': "media/static/web/assets/img/svg/origin-guarantee.svg", 'name': "ضمانت اصل بودن کالا"},
        ]

        self.__banner_data = [
            {'scope': "ss", 'picture': "media/static/web/assets/img/banner/banner-side-slider-1.jpg"},
            {'scope': "ss", 'picture': "media/static/web/assets/img/banner/banner-side-slider-2.jpg"},
            {'scope': "h4", 'picture': "media/static/web/assets/img/banner/small-banner-1.jpg"},
            {'scope': "h4", 'picture': "media/static/web/assets/img/banner/small-banner-2.jpg"},
            {'scope': "h4", 'picture': "media/static/web/assets/img/banner/small-banner-3.jpg"},
            {'scope': "h4", 'picture': "media/static/web/assets/img/banner/small-banner-4.jpg"},
            {'scope': "h2", 'picture': "media/static/web/assets/img/banner/medium-banner-1.jpg"},
            {'scope': "h2", 'picture': "media/static/web/assets/img/banner/medium-banner-2.jpg"},
            {'scope': "h1", 'picture': "media/static/web/assets/img/banner/large-banner.jpg"},
        ]

        self.__slider_data = [
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/1.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/1.jpg"
            },
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/2.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/2.jpg"
            },
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/3.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/3.jpg"
            },
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/4.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/4.jpg"
            },
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/5.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/5.jpg"
            },
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/6.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/6.jpg"
            },
            {
                'res_picture': "media/static/web/assets/img/main-slider/slider-responsive/7.jpg",
                'picture': "media/static/web/assets/img/main-slider/img-slider-2/7.jpg"
            },
        ]

    def create_user(self):
        return get_user_model().objects.create_user(
            username='09109234511',
            password='Hmz1377528',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

    def create_setting(self):
        setting = Setting(
            domain="http://127.0.0.1:8000",
            name="فروشگاه اینترنتی آرکا",
            title="فروشگاه اینترنتی آرکا",
            phone_number="09123334444",
            email="info@saaco.net",
            address="ایران، تهران، شریعتی",
            city="tehran",
            location=Point(51.3896004, 35.6892523),
            summary_about="تاپ کالا به عنوان یکی از قدیمی‌ترین فروشگاه های اینترنتی با بیش از یک دهه تجربه، با پایبندی به سه اصل کلیدی، پرداخت در محل، 7 روز ضمانت بازگشت کالا و تضمین اصل‌بودن کالا، موفق شده تا همگام با فروشگاه‌های معتبر جهان، به بزرگ‌ترین فروشگاه اینترنتی ایران تبدیل شود. به محض ورود به تاپ کالا با یک سایت پر از کالا رو به رو می‌شوید! هر آنچه که نیاز دارید و به ذهن شما خطور می‌کند در اینجا پیدا خواهید کرد.",
            logo_alternate_text=fake.text(30)
        )

        setting.logo = SimpleUploadedFile(
            name=fake.file_name(extension='png'),
            content=open(
                os.path.join(settings.BASE_DIR, 'media/static/web/assets/img/logo.png'
                             ),
                'rb').read(),
            content_type='image/png'
        )

        setting.save()
        return setting

    def create_faq(self):
        faq = Faq(
            question=fake.text(random.randint(50, 80)),
            answer=fake.text(random.randint(120, 180))
        )

        faq.save()
        return faq

    def create_social(self):
        social = Social(
            name=self.__social_name[0],
            link=fake.url(),
        )

        self.__social_name.pop(0)
        social.save()
        return social

    def create_banner(self):
        banner = Banner(
            name=fake.text(10),
            link=fake.url(),
            is_active=True,
            scope=self.__banner_data[0].get('scope'),
            picture_alternate_text=fake.text(30)
        )

        banner.picture = SimpleUploadedFile(
            name=fake.file_name(extension='png'),
            content=open(
                os.path.join(settings.BASE_DIR, self.__banner_data[0].get('picture')),
                'rb').read(),
            content_type='image/png'
        )

        self.__banner_data.pop(0)
        banner.save()
        return banner

    def create_service(self):
        service = Service(
            name=self.__service_data[0].get('name'),
            description=fake.text(50),
            svg_alt_text=fake.text(30)
        )

        service.svg = SimpleUploadedFile(
            name=fake.file_name(extension='svg'),
            content=open(
                os.path.join(settings.BASE_DIR, self.__service_data[0].get('svg')),
                'rb').read(),
            content_type='image/svg'
        )

        self.__service_data.pop(0)
        service.save()
        return service

    def create_contact(self):
        contact = Contact(
            name=fake.name(),
            email=fake.email(),
            phone_number="+989123334444",
            subject=fake.text(30),
            message=fake.text(500),
        )

        contact.save()
        return contact

    def create_slider(self):
        slider = Slider(
            name=fake.text(25),
            picture_alternate_text=fake.text(30),
            is_active=True,
            link=fake.url()
        )

        slider.picture = SimpleUploadedFile(
            name=fake.file_name(extension='png'),
            content=open(
                os.path.join(settings.BASE_DIR, self.__slider_data[0].get('picture')
                             ),
                'rb').read(),
            content_type='image/png'
        )

        slider.res_picture = SimpleUploadedFile(
            name=fake.file_name(extension='png'),
            content=open(
                os.path.join(settings.BASE_DIR, self.__slider_data[0].get('res_picture')
                             ),
                'rb').read(),
            content_type='image/png'
        )

        self.__slider_data.pop(0)
        slider.save()
        return slider

    def process_create(self):
        self.create_user()
        self.create_setting()
        self.create_faq()

        for i in range(len(self.__banner_data)):
            self.create_banner()

        for i in range(len(self.__social_name)):
            self.create_social()

        for i in range(len(self.__service_data)):
            self.create_service()

        for i in range(len(self.__slider_data)):
            self.create_slider()

        return 'Data is generated'


class ProductDataGenerator:
    def __init__(self):
        self.__brand_name = [
            {"name": 'samsung', "picture": "media/static/web/assets/img/brand/1078.png"},
            {"name": 'huawei', "picture": "media/static/web/assets/img/brand/1000006973.png"},
            {"name": 'xiaomi', "picture": "media/static/web/assets/img/brand/Lenovo-Symbol.jpg"},
            {"name": 'oppo', "picture": "media/static/web/assets/img/brand/2315.png"},
            {"name": 'nokia', "picture": "media/static/web/assets/img/brand/1086.png"},
            {"name": 'apple', "picture": "media/static/web/assets/img/brand/apple-logo_318-40184.jpg"},
        ]

        self.__fa_names = list(set([fake_fa.name() for i in range(2000)]))
        self.__en_names = list(set([fake.name() for i in range(1000)]))

        self.__category_data = [
            {'name': "گوشی موبایل", 'ordering': "1", "subs": [
                {'name': "سامسونگ", 'ordering': "1"},
                {'name': "هواوی", 'ordering': "2"},
                {'name': "شیائومی", 'ordering': "3"},
                {'name': "نوکیا", 'ordering': "4"},
                {'name': "اپل", 'ordering': "5"},
                {'name': "اوپو", 'ordering': "6"},
            ]},
            {'name': "لوازم جانبی", 'ordering': "2", "subs": [
                {'name': "قاب موبایل", 'ordering': "1"},
                {'name': "هندزفری", 'ordering': "2"},
                {'name': "مونوپاد", 'ordering': "3"},
            ]},
            {'name': "ساعت هوشمند", 'ordering': "3", "subs": [
                {'name': "اپل واچ", 'ordering': "1"},
                {'name': "سامسونگ واچ", 'ordering': "2"},
                {'name': "هواوی واچ", 'ordering': "3"},
                {'name': "شیائومی واچ", 'ordering': "4"},
            ]},
            {'name': "دوربین عکاسی", 'ordering': "4", "subs": [
                {'name': "کنون", 'ordering': "1"},
                {'name': "نیکون", 'ordering': "2"},
                {'name': "سونی", 'ordering': "3"},
            ]},
            {'name': "لپتاپ و کامپیوتر", 'ordering': "5", "subs": [
                {'name': "dell", 'ordering': "1"},
                {'name': "apple", 'ordering': "2"},
                {'name': "asus", 'ordering': "3"},
                {'name': "lenovo", 'ordering': "4"},
            ]}
        ]

        self.__surety = [
            "گارانتی ۱۸ ماهه مدیا پردازش",
            "گارانتی ۱۸ ماهه دیجی سرویس + بیمه ۱۲ ماهه ایران",
            "گارانتی ۱۸ ماهه پارسا فرتاک داده ی ویرا",
            "گارانتی ۱۸ ماهه داریا همراه پایتخت",
            "گارانتی ۱۸ ماهه آرکا تجارت بیستون",
        ]

        self.__colors = [
            {"name": "قرمز", "type": 'c', "hex": "#ff0000"},
            {"name": "آبی", "type": 'c', "hex": "#0000ff"},
            {"name": "مشکی", "type": 'c', "hex": "#000000"},
            {"name": "سفید", "type": 'c', "hex": "#ffffff"},
        ]

    def create_attribute(self):
        attribute = Attribute(
            name=self.__colors[0].get("name"),
            hex=self.__colors[0].get("hex"),
            type=self.__colors[0].get("type"),
        )

        self.__colors.pop(0)

        attribute.save()
        return attribute

    def create_brand(self):
        brand = Brand(
            title=self.__brand_name[0].get('name'),
            picture_alternate_text=fake.text(20),
            sku='brand' + secrets.token_hex(4)
        )
        brand.picture = SimpleUploadedFile(
            name=fake.file_name(extension='png'),
            content=open(
                os.path.join(settings.BASE_DIR, self.__brand_name[0].get('picture')
                             ),
                'rb').read(),
            content_type='image/png'
        )
        self.__brand_name.pop(0)
        brand.save()
        return brand

    def create_category(self):
        category = Category(
            title=self.__category_data[0].get('name'),
            ordering=self.__category_data[0].get('ordering'),
        )
        category.save()
        return category

    def create_sub_category(self, parent):
        sub_category = Category(
            title=self.__category_data[0].get("subs")[0].get('name'),
            ordering=self.__category_data[0].get("subs")[0].get('ordering'),
            parent=parent
        )
        sub_category.save()
        return sub_category

    def create_tag(self):
        tag = Tag(
            title=self.__fa_names[0],
        )
        self.__fa_names.pop(0)
        tag.save()
        return tag

    def create_product(self, category):
        product = Product(
            title=self.__fa_names[0],
            category=category,
            name=self.__fa_names[0],
            name_en=self.__en_names[0],
            seo_description="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            brand=Brand.objects.order_by('?').first(),
            is_published=True,
            is_installment=fake.boolean(),
            keywords="maiores, exercitationem, nesciunt, recusandae, dicta, cumque, perferendis, laboriosam",
            weight=random.randint(100, 250),
            sales=random.randint(0, 100),
            summary="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.",
            description="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد وزمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد وزمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.",
            specifications=[
                {"group": "مشخصات کلی", "items": [
                    {"key": "ابعاد", "value": "155 میلی متر"},
                    {"key": "ابعاد", "value": "155 میلی متر"},
                    {"key": "ابعاد", "value": "155 میلی متر"}
                ]},
                {"group": "پردازنده", "items": [
                    {"key": "نوع", "value": "155 میلی متر"},
                    {"key": "تایپ", "value": "155 میلی متر"},
                    {"key": "مدل", "value": "155 میلی متر"}
                ]}
            ],
            picture_alternate_text=fake.text(30),
        )
        product.picture = SimpleUploadedFile(
            name=fake.file_name(extension='jpg'),
            content=open(
                os.path.join(settings.BASE_DIR, 'media/static/web/assets/img/products/027.jpg'
                             ),
                'rb').read(),
            content_type='image/jpg'
        )

        self.__fa_names.pop(0)

        product.save()
        return product

    def create_gallery(self, product, gallery_pics):
        gallery = Gallery(
            picture_alternate_text=fake.text(30),
            product=product
        )

        gallery.picture = SimpleUploadedFile(
            name=fake.file_name(extension='jpg'),
            content=open(
                os.path.join(settings.BASE_DIR, gallery_pics[0]),
                'rb').read(),
            content_type='image/jpg'
        )
        gallery_pics.pop(0)
        gallery.save()
        return gallery

    def create_data(self, product, colors):
        total_price = random.randint(50000000, 200000000)
        discount = random.choices([0, 5, 10, 20], [0.6, 0.2, 0.1, 0.1])[0]
        data = Data(
            product=product,
            color=colors[0],
            surety=random.choices(self.__surety[0]),
            total_price=total_price,
            discount=discount,
            price=total_price - (total_price * discount) / 100,
            min_cart=1,
            max_cart=random.randint(3, 8),
            stock=random.randint(10, 100)
        )

        data.save()
        return data

    def create_feature(self, product):
        feature = Feature(
            product=product,
            key=fake.word(),
            value=fake.text(20),
        )
        feature.save()
        return feature

    def process_create(self):
        for _ in range(len(self.__brand_name)):
            self.create_brand()

        for _ in range(len(self.__colors)):
            self.create_attribute()

        for _ in range(30):
            self.create_tag()

        for _ in range(len(self.__category_data)):
            category = self.create_category()
            for _ in range(len(self.__category_data[0].get('subs'))):
                sub_category = self.create_sub_category(parent=category)
                for _ in range(random.randint(10, 15)):
                    product = self.create_product(category=sub_category)

                    product_tags = list(Tag.objects.all().order_by('?'))
                    for _ in range(random.randint(5, 10)):
                        product.tags.add(product_tags[0])
                        product_tags.pop(0)

                    gallery_pictures = [
                        'media/static/web/assets/img/products/026.jpg',
                        'media/static/web/assets/img/products/028.jpg',
                        'media/static/web/assets/img/products/029.jpg',
                    ]

                    for _ in range(len(gallery_pictures)):
                        self.create_gallery(product=product, gallery_pics=gallery_pictures)

                    attributes = list(Attribute.objects.all())

                    for _ in range(len(attributes)):
                        self.create_data(product=product, colors=attributes)
                        attributes.pop(0)

                    for _ in range(10):
                        self.create_feature(product=product)

                self.__category_data[0].get("subs").pop(0)
            self.__category_data.pop(0)

        return 'Data is generated'
