# RobotArm

Dynamixel AX-12A Robotic Arm

COMPONENTS:

===========================CONTROLLER===========================

Raspberry Pi 3B (https://www.adafruit.com/product/3055?src=raspberrypi).

===========================MOTOR===========================

Dynamixel AX-12A (Four) When you purchase the Dynamixel AX-12A motors, they come with a whole bunch of tiny bolts, nuts, plastic washer, etc (https://www.trossenrobotics.com/dynamixel-ax-12-robot-actuator.aspx).

===========================NUTS AND BOLTS===========================

 You will also need some longer bolts to connect the Bioloid Frame F10 to Bioloid Frame F8. I went to my hardware store and purchased the following:

Ten (10): 1-72 x 1/2 Flat Head Phillips ($0.25 x 10)
Ten (10): 1-72 Finished Hex Nut ($0.28 x 10)

You can get these online if you can purchase just 10 of each. Here's an example of a vendor (I have not used them):
https://www.fastenal.com/products/details/0170097
https://www.fastenal.com/products/details/36003

===========================COUPLERS===========================

Bioloid Frame F1 (One)
Bioloid Frame F2 (One – one of these comes with each motor)
Bioloid Frame F3 (Five – each motor comes with one of these)
Bioloid Frame F4 (One)
Bioloid Frame F8 (Two)
Bioloid Frame F10 (Two)
Source: https://www.trossenrobotics.com/robot-parts.aspx

===========================ARM STAND===========================

You are going to need something to hold the arm down with. I happened to have a spare knife block, but you can use anything you like as long as it’s relatively heavy. I like the setup Corgitronics has on YouTube (https://www.youtube.com/watch?v=M20P-k8dF4g&t=314s). He purchased the following:

250mm V-Slot 20x40 Linear Rail (https://openbuildspartstore.com/v-slot-20x40-linear-rail/)
V-Slot Build Plate (https://openbuildspartstore.com/build-plate/)

Low Profile M5 Screws (https://openbuildspartstore.com/low-profile-screws-m5-10-pack/). I would say maybe get 10 short (15mm) and 10 long (25mm)

M5 Tee Nuts (10 Pack) (https://openbuildspartstore.com/tee-nuts-m5-10-pack/)

He also talks about “corner connector blocks” but I’m not sure here. You can certainly ask him on his video (he answers quickly). Video also shows some kind of metal coupler between the 1st motor and the base.

===========================BREADBOARD SETUP ======================

830 Point High Quality Breadboard: (https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=20723)

Resistor 10k Ohm 1/4 Watt 5%:
https://www.jameco.com/z/CF1-4W103JRC-Resistor-Carbon-Film-10k-Ohm-1-4-Watt-5-_691104.html
You don’t want backpower/backfeed to damage the Pi and that’s why you need this resistor.

Tri-State Octal Buffer Line Driver DIP 20 (74LS241):
https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=47167
Raspberry Pi communicates at full-duplex and AX-12A communicates at half-duplex. This IC will manage the communication between full and half duplex.

160 Piece ZipWire Jumper Wire Kit:
https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=2260762

===========================POWER SUPPLY===========================

I purchased a cheapo used power supply from eBay. I’ve had it for a couple of months now and works just fine. I like the power supply better than batteries because batteries drain to quickly.

MASTECH HY1803D LINEAR REGULATED DC POWER SUPPLY VARIABLE 0-18V, 0-3A
https://www.ebay.com/itm/MASTECH-HY1803D-LINEAR-REGULATED-DC-POWER-SUPPLY-VARIABLE-0-18V-0-3A/152882299490?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3D48781d89a74e4b64910c90db1f6967cb%26pid%3D100675%26rk%3D2%26rkt%3D15%26sd%3D253633716678%26itm%3D152882299490&_trksid=p2481888.c100675.m4236&_trkparms=pageci%3Aefc07bee-3ac8-11e9-8966-74dbd1806bf0%7Cparentrq%3A308227e61690ad7934b9d1f4ffe71fbc%7Ciid%3A1

If you purchase it from eBay, make sure you call them (Cogwe11 are in the Bay Area of California) and ask them to include the test-lead-set (the red and black wires you connect to the posts). Wires are not included in the eBay purchase. Be careful with the power supply as you can easily kill yourself with anything over 1 amp.

===========================OTHER===========================

Monitor: I sign up for Fry’s electronics emails and I always see deals on cheap monitors. Here’s an example of what I currently have: https://www.cdw.com/product/HP-22uh-21.5in-LED-backlit-LCD-Black/3685521?cm_cat=google&cm_ite=3685521&cm_pla=NA-NA-HP%20Inc_VL&cm_ven=acquirgy&ev_chn=shop&gclid=Cj0KCQiAh9njBRCYARIsALJhQkFWEewn6JJBX4TEqrSnrCj23q3sXlm1pxhZ3xd5drwOgNQc9Ai1lzQaAjMPEALw_wcB&s_kwcid=AL!4223!3!198537045734!!!g!122626337779!


Keyboard: small form factor wired keyboard is nice. This is what I purchased from my local PC store:
 https://www.cdw.com/product/SIIG-USB-Mini-Multimedia-Keyboard/1871380?cm_cat=google&cm_ite=1871380&cm_pla=NA-NA-SIIG_KB&cm_ven=acquirgy&ev_chn=shop&gclid=Cj0KCQiAh9njBRCYARIsALJhQkH5L4IG3PtQRWV0UttaLFWV3tPVfUYjYSDPTJaMBEuliHSLVlUGa3waAoD3EALw_wcB&s_kwcid=AL!4223!3!198553132047!!!g!300642121139!

Mouse: any kind of wired optical mouse (stay away from wireless anything, that $h*t gives you cancer).

Ram-Pro Helping Hands Magnifier Glass Stand with Alligator Clips – 4x Magnifying Lens, Perfect for Soldering, Crafting & Inspecting Micro Objects
https://www.amazon.com/Ram-Pro-Helping-Hands-Magnifier-Alligator/dp/B078SY5DPZ/ref=sr_1_5?keywords=helping+hands&qid=1551297695&s=office-products&sr=1-5

This is my inspiration video for this project:
https://www.youtube.com/watch?v=M-LKlea_6Vs



SOFTWARE:
change IDs

