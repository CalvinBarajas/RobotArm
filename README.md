<h1>RobotArm ($315 to $500 + Tax + S&H)</h1>
<h4>Estimated Avg Cost: $215 (Most People Have Some Of The Components Already)</h4>

<p>In this project, you want to proceed slowly (I cannot emphasize this enough). Add one motor, and see how it behaves. Add a second motor, and see how they both behave, and so on. Make sure you study the documentation (links provided below) and familiarize yourself with how the technology works. It took me about 5 weeks of working full-time to get to this point. I had to learn electricity (current, amps, voltage, capacitors, resistors, etc.), python, Linux, UART, and on and on and on. You can benefit from my hard work in this project.</p>

<hr />
<h3>CONTROLLER ($35)</h3>
<hr />

<p>&nbsp;&nbsp;&nbsp;&bull;
Raspberry Pi 3B (https://www.adafruit.com/product/3055?src=raspberrypi).</p>

<hr />
<h3>MOTORS ($180)</h3>
<hr />

<p>&nbsp;&nbsp;&nbsp;&bull; 
Dynamixel AX-12A (Four) When you purchase the Dynamixel AX-12A motors, they come with a whole bunch of tiny bolts, nuts, plastic washer, etc (https://www.trossenrobotics.com/dynamixel-ax-12-robot-actuator.aspx).</p>

<hr />
<h3>NUTS AND BOLTS ($8)</h3>
<hr />

<p>You will also need some longer bolts to connect the Bioloid Frame F10 to Bioloid Frame F8 and Bioloid Frame F3 to Bioloid Frame F4. I went to my hardware store and purchased the following:</p>

<ul>
 <li>(qty 14): 1-72 x 1/2 Flat Head Phillips ($0.25)</li>
 <li>(qty 14): 1-72 Finished Hex Nut ($0.28)</li>
</ul>

<p>You can order these online if you can purchase in small quantities. Please note that the 1-72 nut is slightly smaller than the nuts that come with the AX-12A (not a big deal at all). Here's an example of a vendor which I have never used but seems to sell in small quantities (let me know if you find a good online vendor, and I can update these links):</p>

<ul>
<li>https://www.fastenal.com/products/details/0170097</li>
<li>https://www.fastenal.com/products/details/36003</li>
</ul>

<hr />
<h3>COUPLERS ($10 to $18)</h3>
<hr />

<p>Take a look at the video I made and you can pretty easily see how each one of the following fits into the arm.</p>

<ul>
<li>Bioloid Frame F1 (qty: 1)</li>
<li>Bioloid Frame F2 (qty: 1) Note: one of these comes with each motor</li>
<li>Bioloid Frame F3 (qty: 5) Note: each motor comes with one of these</li>
<li>Bioloid Frame F4 (qty: 1)</li>
<li>Bioloid Frame F8 (qty: 2)</li>
<li>Bioloid Frame F10 (qty: 2)</li>
<li>Source: https://www.trossenrobotics.com/robot-parts.aspx</li>
</ul>

<p>I perused this video like the Dead Sea Scrolls in order to find out exactly how everything fit together: https://www.youtube.com/watch?v=M-LKlea_6Vs</p>

<hr />
<h3>ARM STAND ($10 to $30)</h3>
<hr />

<p>You are going to need something to hold the arm down with. I happened to have a spare knife block, but you can use anything you like as long as it’s relatively heavy. You can also purchase a block of wood at your lumber store. I nailed my Bioloid Frame F3 to the knife block but you may want to purchase small wood screws (tiny) instead. By using nails, it's a nightmare to take off. I also like the setup Corgitronics has on YouTube (https://www.youtube.com/watch?v=M20P-k8dF4g&t=314s). He purchased the following:</p>

<ul>
<li>250mm V-Slot 20x40 Linear Rail (https://openbuildspartstore.com/v-slot-20x40-linear-rail/)</li>
<li>V-Slot Build Plate (https://openbuildspartstore.com/build-plate/)</li>
<li>Low Profile M5 Screws (https://openbuildspartstore.com/low-profile-screws-m5-10-pack/). I would say maybe get 10 short (15mm) and 10 long (25mm)</li>
<li>M5 Tee Nuts (10 Pack) (https://openbuildspartstore.com/tee-nuts-m5-10-pack/)</li>
</ul>

<p>He also talks about “corner connector blocks” but I’m not sure here. You can certainly ask him on his video (he answers quickly). Video also shows some kind of metal coupler between the 1st motor and the base.</p>

<hr />
<h3>BREADBOARD SETUP ($30 to $50)</h3>
<hr />

<ul>

<li><strong>830 Point High Quality Breadboard:</strong> (https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=20723)<br />
Note: Don't purchase the cheap breadboards from Amazon. They are usually made with inferior materials and markings are off.</li>

<li><strong>10k Ohm 1/4 Watt 5% Resistor:</strong> (https://www.jameco.com/z/CF1-4W103JRC-Resistor-Carbon-Film-10k-Ohm-1-4-Watt-5-_691104.html).<br />
Note: You don’t want backpower/backfeed to damage the Pi and that’s why you need this resistor. You may just want to get a whole set with different sizes if you plan to do a lot of electronics work.</li>

<li><strong>Tri-State Octal Buffer Line Driver DIP 20 (74LS241):</strong> https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=47167.<br />
Note: Raspberry Pi communicates at full-duplex and AX-12A communicates at half-duplex. This IC will manage the communication between full and half duplex.</li>

<li><strong>160 Piece ZipWire Jumper Wire Kit:</strong> https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=2260762<br />
Note: This kit is a good starting point. If you want to make your own sizes and plan on doing a lot of projects, I would recommend the assortment below.</li>

<li><strong>(OPTIONAL) 22AWG 6-Color Tinned-Copper Wire Assortment:</strong> 
https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?langId=-1&storeId=10001&catalogId=10001&productId=2153705<br />
Note: I love this set because it has all the wire colors we need, you can cut any length, and the wire is thick enough to penetrate breadboard holes nicely.</li>

<li><strong>(OPTIONAL) 7-in-1 Tool Hand HT-1042 26-16AWG Wire Stripper:</strong> 
https://www.jameco.com/z/HT-1042-R-Hanlong-Tools-7-in-1-Tool-Hand-HT-1042-26-16AWG-Wire_127862.html?CID=MERCH<br />
Note: You want to get a wire stripper like this one because working with the 22AWG wires above will be easier.</li>

<li><strong>(OPTIONAL) JIALIUJ Pick Up Tools Powerful Four Claw Paws Parts Chip Grabber Screw Precision Components Part Gripper Hand Tool Set</strong> https://www.amazon.com/JIALIUJ-Powerful-Grabber-Precision-Components/dp/B07NY823HP/ref=sr_1_4?keywords=screw+pickup+tool+claw&qid=1552153887&s=industrial&sr=1-4<br />
Note: When working with super tiny nuts and bolts, this tool is a real life saver. You can also purchase plastic versions of this one for $3.00 at a computer store.</li>

</ul>

<hr />
<h3>POWER SUPPLY ($40)</h3>
<hr />

<p>I purchased a cheapo used power supply from eBay. I’ve had it for a couple of months now and works just fine. I like the power supply better than batteries because batteries drain too quickly.</p>

<ul>
<li>MASTECH HY1803D LINEAR REGULATED DC POWER SUPPLY VARIABLE 0-18V, 0-3A: https://www.ebay.com/itm/MASTECH-HY1803D-LINEAR-REGULATED-DC-POWER-SUPPLY-VARIABLE-0-18V-0-3A/152882299490?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3D48781d89a74e4b64910c90db1f6967cb%26pid%3D100675%26rk%3D2%26rkt%3D15%26sd%3D253633716678%26itm%3D152882299490&_trksid=p2481888.c100675.m4236&_trkparms=pageci%3Aefc07bee-3ac8-11e9-8966-74dbd1806bf0%7Cparentrq%3A308227e61690ad7934b9d1f4ffe71fbc%7Ciid%3A1</li>
</ul>

<p>If you purchase it from eBay, make sure you call them (Cogwe11 are in the Bay Area of California) and ask them to include the test-lead-set (the red and black wires you connect to the posts). Wires are not included in the eBay purchase. Be careful with the power supply as you can easily kill yourself with anything over 1 amp.</p>

<hr />
<h3>OTHER ($142)</h3>
<hr />

<ul>

<li><strong>Monitor:</strong> I sign up for Fry’s electronics emails and I always see deals on cheap monitors. Here’s an example of what I currently have: https://www.cdw.com/product/HP-22uh-21.5in-LED-backlit-LCD-Black/3685521?cm_cat=google&cm_ite=3685521&cm_pla=NA-NA-HP%20Inc_VL&cm_ven=acquirgy&ev_chn=shop&gclid=Cj0KCQiAh9njBRCYARIsALJhQkFWEewn6JJBX4TEqrSnrCj23q3sXlm1pxhZ3xd5drwOgNQc9Ai1lzQaAjMPEALw_wcB&s_kwcid=AL!4223!3!198537045734!!!g!122626337779!</li>

<li><strong>Keyboard:</strong> small form factor wired keyboard is nice. This is what I purchased from my local PC store: https://www.cdw.com/product/SIIG-USB-Mini-Multimedia-Keyboard/1871380?cm_cat=google&cm_ite=1871380&cm_pla=NA-NA-SIIG_KB&cm_ven=acquirgy&ev_chn=shop&gclid=Cj0KCQiAh9njBRCYARIsALJhQkH5L4IG3PtQRWV0UttaLFWV3tPVfUYjYSDPTJaMBEuliHSLVlUGa3waAoD3EALw_wcB&s_kwcid=AL!4223!3!198553132047!!!g!300642121139!</li>

<li><strong>Mouse:</strong> any kind of wired optical mouse (stay away from wireless anything, that $h*t gives you cancer).</li>

<li><strong>Ram-Pro Helping Hands Magnifier Glass Stand with Alligator Clips</strong> – 4x Magnifying Lens, Perfect for Soldering, Crafting & Inspecting Micro Objects https://www.amazon.com/Ram-Pro-Helping-Hands-Magnifier-Alligator/dp/B078SY5DPZ/ref=sr_1_5?keywords=helping+hands&qid=1551297695&s=office-products&sr=1-5</li>

</ul>

<p>This is my inspiration video for this project: https://www.youtube.com/watch?v=M-LKlea_6Vs</p>

<hr />
<h3>SOFTWARE</h3>
<hr />

<p><strong>Files (Code) Included In This Repository:</strong></p>

<ul>
 <li>How to change motor IDs (dynamixel_write_ID.py). I'm using 1, 2, 3, 4 (4 is the hand motor, 1 is the shoulder motor)</li>
 <li>Slow motor movement (arm_project_slow_movement.py). Use this when you are starting out and be ready to kill power if the motors are not behaving as expected.</li>
 <li>Fast motor movement (arm_project_fast_movement.py). You can use this on the final project to speed things up a bit.</li>
</ul>

<hr />
<h3>USEFUL REFERENCE MATERIAL</h3>
<hr />

<ul>

<li><p><strong>Wiring Diagram:</strong> https://github.com/jeremiedecock/pyax12<br />
Note: This French dude (Jérémie Decock) is a genius. Follow the diagram to connect all the cables in the breadboard.</p></li>

<li><p><strong>AX-12A Control Table (2019):</strong> http://emanual.robotis.com/docs/en/dxl/ax/ax-12a/<br />
Note: The AX-12A motors are a "register" based motor. This means you write and read from a table. At first this can be hella confusing but once you understand the basics it makes sense. Pay particular attention to goal position because this will tell you exactly where the motor should be. You might come across some older manuals that are a good reference, but put most of your reading effort into the newer documents listed here. I printed all the documentation onto PDFs, and I annotated the $h*t out of them using Adobe on my PC.</p></li>

<li><p><strong>Instruction & Status Packets (2019):</strong> http://emanual.robotis.com/docs/en/dxl/protocol1/<br />
Note: They have a great explanation of how instruction packets and status packets are created. They also have a lot of examples.</p></li>

<li><p><strong>How To Setup Hardware & Sample Code:</strong> http://www.oppedijk.com/robotics/control-dynamixel-with-raspberrypi<br />
Note: There are a couple of mistakes on this page, but this is what I used initially. The circuit diagram instructions are pretty solid.</p></li>

<li><p><strong>Raspberry Pi Pinout: https:</strong> http://pinout.xyz/<br />
Note: Excellent for learning all the pins.</p></li>

<li><p><strong>Everything You Want to Know About Raspberry Pi GPIO: But Were Afraid to Ask:</strong> https://www.circuits.dk/everything-about-raspberry-gpio/<br />
Note: One of the most comprehensive Pi resources I've found.</p></li>

<li><p><strong>Controlling AX-12A With 74LS241:</strong> https://memememememememe.me/post/the-dynamixel-ax-12a-servos/<br />
Note: This was one of the original documents I used in order to get started. It has a good explanation of why 74LS241 is needed.</p></li>

<li><p><strong>Checksum Calculator:</strong> http://easyonlineconverter.com/converters/checksum_converter.html <br />
Note: Useful tool for calculating checksum. You may also want to take a look at a very good explanation on how to calculate checksum: https://www.digi.com/resources/documentation/Digidocs/90002002/Tasks/t_calculate_checksum.htm?TocPath=API%20Operation%7CAPI%20frame%20format%7C_____1</p></li>

</ul>


<hr />
<h3>STEP-BY-STEP SETUP INSTRUCTIONS</h3>
<hr />

<ul>

<li><strong>Step 01:</strong> Purchase controller, motors, nuts and bolts, couplers, arm stand, breadboard, power supply, monitor, keyboard, mouse, helping hands, etc.</li>

<li><strong>Step 02:</strong> Connect KVM to Pi (KVM = keyboard, video, mouse). Place the Pi on a non-conductive surface (ceramic, wood, plastic).</li>

<li><strong>Step 03:</strong> Format SD card, install Raspbian on Pi, connect to the net, update software to latest. Many videos on YouTube cover this. Enable serial port and disable serial console in Pi config utility.</li>

<li><strong>Step 04:</strong> Wire up breadboard with 74LS241 IC (see wiring diagram link above). Be sure to use same color wires if possible. I also purchased a set (22AWG 6-Color Tinned-Copper Wire Assortment) from Jameco (see links above) and have been very happy with the quality. The 22AWG wire is very nice and "thick" (not the flimsy thin-wire kind). Just make sure you have wire strippers in order to cut the length you want. BTW, I'm not pushing Jameco at all. You can purchase from anywhere on the web. The reason I like Jameco is because it's local to me and they sell in small quantities.</li>

<li><strong>Step 05:</strong> Connect your breadboard to power supply using the alligator clips on the helping hands (see video). Turn the knobs of the power supply way down before you start. Increase the voltage knob up to 9.5 volts (you don't have to touch amp knob, just make sure it's way down).</li>

<li><strong>Step 06:</strong> Connect each motor one-by-one and change the motor's ID (1, 2, 3, 4). Check the wiring diagram before connecting anything. Basically, CABLE-20 (250mm 3-pin) that came with your motor (a.k.a., servo, actuator, etc.) connects to the left-hand-side (looking at the motor from the back) so that the GND (ground) pin is facing the middle part of the motor. There are a ton of diagrams on the web showing you this.</li>

<li><strong>Step 07:</strong> Once the IDs are set, begin assembling the arm. Start with motor 1 (shoulder) and play with the code. Add motor 2 and play with the code some more, repeat for the remaining motors testing and observing along the way. Once you have a fully assembled arm, bring power up to 11.1 VDC (volts direct current).</li>

<li><strong>Step 08:</strong> Now film your working arm and upload it to YouTube.</li>

</ul>

<p>Check it out on Instructables.com: https://www.instructables.com/id/RobotArm-2/</p>
<p>Check it out on YouTube: https://www.youtube.com/channel/UCY6rwa3NrBVojsvjdOysjrA?view_as=subscriber</p>

<p>eof</p>

