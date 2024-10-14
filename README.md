این پروژه شامل دو اسکریپت Python است که داده‌های نمونه را در جداول مختلف در ClickHouse وارد می‌کنند. 
از ماژول‌های random و names برای تولید داده‌ها و از کتابخانه‌ی clickhouse_connect برای اتصال و تعامل با پایگاه داده‌ی ClickHouse استفاده می‌شود.

پیش‌نیازها
نصب ClickHouse و اجرای آن - نصب python - نصب پکیج‌های موردنیاز: 
pip install clickhouse-connect names

**پروژه Project Assignments:**
این اسکریپت جدول project_assignments را ایجاد می‌کند و داده‌هایی شامل ۵۰ آی‌دی به همراه نام پروژه‌ها را به‌طور تصادفی وارد جدول می‌کند.

**جزئیات اسکریپت:**

ایجاد جدول project_assignments با ستون‌های ID و Project_Name.
تولید ۵۰ ردیف داده با انتخاب تصادفی نام پروژه از لیستی از پروژه‌ها.

پ**روژه salary:**

این اسکریپت جدول company1403 را ایجاد کرده و داده‌هایی شامل نام کامل، دپارتمان و حقوق برای ۵۰ نفر از کارمندان را تولید و به ClickHouse اضافه می‌کند.

**جزئیات اسکریپت:**

ایجاد جدول company1403 با ستون‌های ID، NAME، DEPARTMENT و SALARY.
تولید ۵۰ ردیف داده با استفاده از نام‌های واقعی (با کتابخانه names)، دپارتمان و حقوق تصادفی.

**نحوه اجرا**
۱. مطمئن شوید که ClickHouse در حال اجرا است. 
۲. هر کدام از اسکریپت‌ها را به صورت زیر اجرا کنید:
python script_name.py

پس از اجرای موفقیت‌آمیز، پیام "Data inserted successfully into ClickHouse!" نمایش داده می‌شود.

**خروجی**
خروجی هر دو اسکریپت در جدول‌های موردنظر در ClickHouse قرار می‌گیرد که می‌توان آن‌ها را برای تحلیل‌های مختلف به کار برد.
