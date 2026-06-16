from models import PhysicalProduct, DigitalProduct

def load_mock_products(stock_manager):
    # Helper functions to generate specs based on category
    def get_laptop_specs():
        return {
            "RAM": "16GB DDR5", "Storage": "1TB NVMe SSD", 
            "Processor": "Intel Core i7 / AMD Ryzen 7", "Display": "14-16 inch QHD", "OS": "Windows 11 Pro"
        }
    def get_keyboard_specs():
        return {
            "Switch Type": "Tactile Mechanical", "Connectivity": "Bluetooth & USB-C", 
            "Backlight": "RGB", "Battery Life": "Up to 72 hours", "Layout": "75% / TKL"
        }
    def get_mouse_specs():
        return {
            "Sensor": "High-Precision Optical", "DPI": "Up to 16,000", 
            "Buttons": "6 Programmable", "Connectivity": "2.4GHz Wireless & Bluetooth"
        }
    def get_monitor_specs():
        return {
            "Resolution": "4K UHD (3840 x 2160)", "Refresh Rate": "144Hz", 
            "Panel Type": "IPS", "Response Time": "1ms (GtG)", "Ports": "HDMI 2.1, DisplayPort 1.4"
        }
    def get_audio_specs():
        return {
            "Driver Size": "40mm / 50mm", "Frequency Response": "20Hz - 20kHz", 
            "Connectivity": "Bluetooth 5.0 / Wired", "Features": "Active Noise Cancellation"
        }
    def get_generic_tech_specs():
        return {
            "Brand": "TechLoom Basics", "Material": "Premium Aluminum / Plastic", 
            "Warranty": "1 Year Limited", "Compatibility": "Universal PC/Mac"
        }

    # ==========================================
    # Physical Products
    # ==========================================
    physical_items = [
        # Laptops & Computers
        ("Gaming Laptop RTX 4080", 185000.00, "LAP-GAM-001", "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=500&q=60", 5, 2.5, 500.00, {"RAM": "32GB DDR5", "Storage": "2TB Gen4 SSD", "GPU": "NVIDIA RTX 4080 16GB", "Processor": "Intel i9 14th Gen", "Display": "16-inch 240Hz Mini-LED"}),
        ("Ultrabook Pro 14", 120000.00, "LAP-ULT-002", "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=500&q=60", 12, 1.2, 300.00, get_laptop_specs()),
        ("Developer Workstation PC", 250000.00, "PC-WRK-003", "https://images.unsplash.com/photo-1587831990711-23ca6441447b?auto=format&fit=crop&w=500&q=60", 3, 15.0, 1500.00, {"RAM": "64GB ECC", "Storage": "4TB NVMe + 8TB HDD", "Processor": "AMD Threadripper PRO", "GPU": "NVIDIA RTX 6000 Ada"}),
        ("Budget Student Laptop", 45000.00, "LAP-STU-004", "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=500&q=60", 20, 1.8, 350.00, {"RAM": "8GB DDR4", "Storage": "512GB SSD", "Processor": "Intel Core i3 12th Gen"}),
        ("Mini PC Home Server", 35000.00, "PC-MIN-005", "https://images.unsplash.com/photo-1550029402-226115b7c579?auto=format&fit=crop&w=500&q=60", 8, 0.9, 200.00, {"RAM": "16GB SODIMM", "Storage": "1TB SSD", "Processor": "Intel N100", "Networking": "Dual 2.5GbE"}),
        
        # Keyboards
        ("Mechanical Keyboard K2", 8500.00, "KEY-MECH-006", "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=500&q=60", 10, 0.8, 150.00, get_keyboard_specs()),
        ("Wireless Ergonomic Keyboard", 6500.00, "KEY-ERG-007", "https://images.unsplash.com/photo-1563298258-00411eb342da?auto=format&fit=crop&w=500&q=60", 15, 0.7, 150.00, get_keyboard_specs()),
        ("RGB Gaming Keyboard", 12000.00, "KEY-GAM-008", "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?auto=format&fit=crop&w=500&q=60", 7, 1.1, 200.00, {"Switch Type": "Linear Optical", "Polling Rate": "8000Hz", "Backlight": "Per-key RGB"}),
        ("Minimalist Bluetooth Keyboard", 4000.00, "KEY-MIN-009", "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=500&q=60", 25, 0.5, 100.00, get_keyboard_specs()),
        ("Custom Artisan Keycaps (Set)", 3500.00, "KEY-CAP-010", "https://images.unsplash.com/photo-1589578228447-e1a4e481c6c8?auto=format&fit=crop&w=500&q=60", 30, 0.2, 50.00, {"Material": "PBT Double-shot", "Profile": "Cherry Profile", "Keys Count": "104"}),

        # Mice
        ("Wireless Gaming Mouse", 7500.00, "MOU-GAM-011", "https://images.unsplash.com/photo-1527814050087-379381547949?auto=format&fit=crop&w=500&q=60", 18, 0.2, 100.00, get_mouse_specs()),
        ("Ergonomic Vertical Mouse", 4500.00, "MOU-ERG-012", "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=500&q=60", 22, 0.2, 100.00, get_mouse_specs()),
        ("Travel Bluetooth Mouse", 2000.00, "MOU-TRV-013", "https://images.unsplash.com/photo-1590212151175-e58edd96185b?auto=format&fit=crop&w=500&q=60", 40, 0.1, 50.00, get_mouse_specs()),
        ("Professional Design Mouse", 8500.00, "MOU-PRO-014", "https://images.unsplash.com/photo-1586816879360-004f5b0c51e3?auto=format&fit=crop&w=500&q=60", 10, 0.2, 100.00, get_mouse_specs()),
        ("Trackball Mouse", 6000.00, "MOU-TRK-015", "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?auto=format&fit=crop&w=500&q=60", 5, 0.3, 100.00, get_mouse_specs()),

        # Monitors
        ("27-inch 4K Designer Monitor", 35000.00, "MON-4K-016", "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=500&q=60", 8, 6.5, 600.00, get_monitor_specs()),
        ("34-inch Ultrawide Gaming Monitor", 45000.00, "MON-ULT-017", "https://images.unsplash.com/photo-1552831388-6a0b35077328?auto=format&fit=crop&w=500&q=60", 4, 8.0, 800.00, {"Resolution": "3440 x 1440", "Refresh Rate": "175Hz", "Panel Type": "OLED", "Response Time": "0.1ms"}),
        ("24-inch 1080p Office Monitor", 12000.00, "MON-OFF-018", "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=500&q=60", 30, 4.0, 400.00, {"Resolution": "1920 x 1080", "Refresh Rate": "75Hz", "Panel Type": "IPS"}),
        ("Portable 15-inch USB-C Monitor", 18000.00, "MON-PRT-019", "https://images.unsplash.com/photo-1586816879360-004f5b0c51e3?auto=format&fit=crop&w=500&q=60", 15, 1.0, 200.00, get_monitor_specs()),
        ("32-inch Curved Monitor", 28000.00, "MON-CRV-020", "https://images.unsplash.com/photo-1616423640778-28d1b53229bd?auto=format&fit=crop&w=500&q=60", 6, 7.0, 700.00, get_monitor_specs()),

        # Audio
        ("Noise Cancelling Headphones", 25000.00, "AUD-ANC-021", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=500&q=60", 25, 0.5, 150.00, get_audio_specs()),
        ("Studio Monitor Speakers (Pair)", 30000.00, "AUD-SPK-022", "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=500&q=60", 10, 8.0, 800.00, get_audio_specs()),
        ("Wireless Earbuds Pro", 18000.00, "AUD-EAR-023", "https://images.unsplash.com/photo-1572569432711-7f6c6f1a95e2?auto=format&fit=crop&w=500&q=60", 40, 0.1, 50.00, get_audio_specs()),
        ("USB Condenser Microphone", 8000.00, "AUD-MIC-024", "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=500&q=60", 15, 1.2, 200.00, {"Polar Pattern": "Cardioid", "Sample Rate": "192kHz/24-bit"}),
        ("Gaming Headset with Surround", 12000.00, "AUD-GAM-025", "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&w=500&q=60", 20, 0.6, 150.00, get_audio_specs()),

        # Networking, Storage & Accessories
        ("Wi-Fi 6 Mesh Router System", 22000.00, "NET-RTR-026", "https://images.unsplash.com/photo-1558346490-a72e53ae50b4?auto=format&fit=crop&w=500&q=60", 12, 1.5, 250.00, {"Wi-Fi Standard": "Wi-Fi 6 (802.11ax)", "Coverage": "Up to 5000 sq ft", "Speed": "AX3000"}),
        ("1TB NVMe PCIe 4.0 SSD", 10000.00, "STR-SSD-027", "https://images.unsplash.com/photo-1597845604169-d9d300e84bfa?auto=format&fit=crop&w=500&q=60", 50, 0.1, 50.00, {"Interface": "PCIe Gen4 x4", "Read Speed": "7300 MB/s", "Write Speed": "6000 MB/s"}),
        ("2TB Portable External HDD", 6500.00, "STR-HDD-028", "https://images.unsplash.com/photo-1563298258-00411eb342da?auto=format&fit=crop&w=500&q=60", 35, 0.3, 100.00, {"Interface": "USB 3.2 Gen 1", "Form Factor": "2.5-inch"}),
        ("4-Bay NAS Enclosure", 45000.00, "STR-NAS-029", "https://images.unsplash.com/photo-1550029402-226115b7c579?auto=format&fit=crop&w=500&q=60", 5, 4.0, 500.00, {"Drive Bays": "4 x 3.5/2.5-inch", "Processor": "Intel Celeron Quad-Core", "RAM": "4GB DDR4"}),
        ("USB-C 10-in-1 Hub", 4500.00, "ACC-HUB-030", "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=500&q=60", 45, 0.2, 100.00, get_generic_tech_specs()),
        ("Extra Large Desk Mat", 2000.00, "ACC-MAT-031", "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=500&q=60", 50, 0.8, 150.00, {"Dimensions": "900mm x 400mm", "Material": "Vegan Leather"}),
        ("Adjustable Laptop Stand", 3500.00, "ACC-STD-032", "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=500&q=60", 30, 1.5, 200.00, get_generic_tech_specs()),
        ("Webcam 1080p 60fps", 6000.00, "ACC-CAM-033", "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=500&q=60", 25, 0.3, 100.00, {"Resolution": "1080p", "Framerate": "60 fps", "FOV": "78 degrees"}),
        ("Monitor Light Bar", 4500.00, "ACC-LGT-034", "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=500&q=60", 20, 0.5, 150.00, get_generic_tech_specs()),
        ("Cable Management Kit", 1500.00, "ACC-CBL-035", "https://images.unsplash.com/photo-1589578228447-e1a4e481c6c8?auto=format&fit=crop&w=500&q=60", 100, 0.4, 100.00, get_generic_tech_specs())
    ]

    for name, price, sku, img, stock, weight, shipping, specs in physical_items:
        stock_manager.add_product(PhysicalProduct(
            name=name, price=price, sku=sku, image_url=img, 
            stock_quantity=stock, shipping_weight=weight, shipping_cost=shipping,
            specifications=specs
        ))

    # ==========================================
    # Digital Products (Software, E-Books, Courses)
    # ==========================================
    
    def get_software_specs():
        return {"License Type": "1 Year Subscription", "Platform": "Windows / macOS / Linux", "Delivery": "Email & Dashboard"}
    def get_ebook_specs():
        return {"File Format": "PDF / EPUB", "Language": "English", "DRM": "Free", "Pages": "Approx 300"}
    def get_course_specs():
        return {"Format": "HD Video Lectures", "Access": "Lifetime", "Certificate": "Yes upon completion"}

    digital_items = [
        # Software Licenses
        ("Pro IDE License Key (1 YR)", 3500.00, "LIC-IDE-036", "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=500&q=60", "/licenses/view/LIC-IDE-036", "1 KB", get_software_specs()),
        ("Photo Editing Suite (Lifetime)", 15000.00, "LIC-PHO-037", "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=500&q=60", "/downloads/photo_suite_installer.exe", "2.4 GB", {"License Type": "Lifetime", "Platform": "Windows/macOS"}),
        ("Video Editor Pro (1 YR)", 12000.00, "LIC-VID-038", "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=500&q=60", "/downloads/video_editor_installer.dmg", "4.1 GB", get_software_specs()),
        ("Antivirus Total Security (1 YR)", 1500.00, "LIC-ANT-039", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=500&q=60", "/downloads/antivirus_setup.exe", "350 MB", get_software_specs()),
        ("Cloud Storage 1TB (1 YR)", 5000.00, "LIC-CLD-040", "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=500&q=60", "/account/activate/cloud", "1 KB", get_software_specs()),

        # E-Books
        ("Python Mastery E-Book", 999.00, "EBK-PY-041", "https://images.unsplash.com/photo-1526379095098-d400fd0bfce8?auto=format&fit=crop&w=500&q=60", "/downloads/python_mastery.pdf", "15 MB", {"File Format": "PDF", "Language": "English", "Pages": "450"}),
        ("Clean Architecture in Practice", 1200.00, "EBK-ARC-042", "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=500&q=60", "/downloads/clean_arch.epub", "8 MB", get_ebook_specs()),
        ("Machine Learning Crash Course", 1500.00, "EBK-ML-043", "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=500&q=60", "/downloads/ml_course.pdf", "22 MB", get_ebook_specs()),
        ("Frontend Frameworks 2026", 800.00, "EBK-FRN-044", "https://images.unsplash.com/photo-1555099962-4199c345e5dd?auto=format&fit=crop&w=500&q=60", "/downloads/frontend_2026.pdf", "10 MB", get_ebook_specs()),
        ("The Complete Docker Guide", 1100.00, "EBK-DOC-045", "https://images.unsplash.com/photo-1605745341112-85968b19335b?auto=format&fit=crop&w=500&q=60", "/downloads/docker_guide.pdf", "18 MB", get_ebook_specs()),

        # Online Courses
        ("Full-Stack Web Dev Bootcamp", 8500.00, "CRS-WEB-046", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=500&q=60", "/courses/enroll/CRS-WEB-046", "Access Link", get_course_specs()),
        ("Advanced Data Structures in C++", 4500.00, "CRS-CPP-047", "https://images.unsplash.com/photo-1551033406-611cf9a28f67?auto=format&fit=crop&w=500&q=60", "/courses/enroll/CRS-CPP-047", "Access Link", get_course_specs()),
        ("UI/UX Design Masterclass", 6000.00, "CRS-DES-048", "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=500&q=60", "/courses/enroll/CRS-DES-048", "Access Link", get_course_specs()),
        ("DevOps Engineering Path", 9000.00, "CRS-DEV-049", "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&w=500&q=60", "/courses/enroll/CRS-DEV-049", "Access Link", get_course_specs()),
        ("Mobile App Dev with React Native", 5500.00, "CRS-MOB-050", "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=500&q=60", "/courses/enroll/CRS-MOB-050", "Access Link", get_course_specs()),

        # Templates & Assets
        ("Premium Website Template Bundle", 2500.00, "AST-WEB-051", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=500&q=60", "/downloads/templates_bundle.zip", "450 MB", {"Format": "HTML/React", "License": "Commercial"}),
        ("Royalty-Free Sound Effects Pack", 1800.00, "AST-SND-052", "https://images.unsplash.com/photo-1511379938547-c1f69419868d?auto=format&fit=crop&w=500&q=60", "/downloads/sfx_pack.zip", "1.2 GB", {"Format": "WAV / MP3", "License": "Commercial"}),
        ("High-Res UI Icon Set", 1200.00, "AST-ICO-053", "https://images.unsplash.com/photo-1558655146-d09347e92766?auto=format&fit=crop&w=500&q=60", "/downloads/icon_set.zip", "50 MB", {"Format": "SVG / PNG", "License": "Commercial"}),
        ("Video Transitions Pack", 3000.00, "AST-VID-054", "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=500&q=60", "/downloads/video_transitions.zip", "3.5 GB", {"Compatibility": "Premiere Pro, DaVinci Resolve"}),
        ("3D Model Library (Game Dev)", 5000.00, "AST-3DM-055", "https://images.unsplash.com/photo-1615469490217-1065ce7d7162?auto=format&fit=crop&w=500&q=60", "/downloads/3d_models.zip", "8.5 GB", {"Format": "FBX / OBJ", "Rigged": "Yes"})
    ]

    for name, price, sku, img, link, size, specs in digital_items:
        stock_manager.add_product(DigitalProduct(
            name=name, price=price, sku=sku, image_url=img, 
            stock_quantity=999999, # Infinite stock for digital
            download_link=link, file_size=size,
            specifications=specs
        ))
