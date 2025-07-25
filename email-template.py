import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

SMTP_SERVER = "server.hosting3.acm.org"
SMTP_PORT = 465
load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

SUBJECT = "Invitation for Students to Participate in PBCTF 4.0"

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PBCTF 4.0 Hackathon Invitation</title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Roboto:wght@300;400;500&display=swap');
    
    body {
      background-color: #000000;
      color: #d0f0c0;
      font-family: 'Roboto', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      line-height: 1.6;
    }
    
    .container {
      max-width: 800px;
      margin: 20px auto;
      background: linear-gradient(135deg, #0a0a0a 0%, #111111 100%);
      padding: 40px;
      border-radius: 15px;
      box-shadow: 0 0 30px rgba(0, 255, 0, 0.3);
    }
    
    .header {
      text-align: center;
      border-bottom: 1px solid rgba(0, 255, 0, 0.3);
      padding-bottom: 25px;
      margin-bottom: 30px;
    }
    
    .logo {
      font-family: 'Orbitron', sans-serif;
      font-size: 2.5rem;
      margin: 0;
      background: linear-gradient(90deg, #0be76ece, #00cc66);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: 2px;
    }
    
    .tagline {
      font-style: italic;
      color: #a0a0a0;
      margin-top: 5px;
      font-size: 1.1rem;
    }
    
    h1, h2, h3 {
      font-family: 'Orbitron', sans-serif;
      color: #0be76ece;
      margin-top: 30px;
      margin-bottom: 15px;
    }
    
    h2 {
      border-bottom: 1px solid rgba(22, 117, 22, 0.877);
      padding-bottom: 8px;
      font-size: 1.4rem;
    }
    
    p {
      font-size: 16px;
      color: #c0c0c0;
      line-height: 1.8;
      margin-bottom: 15px;
    }
    
    .highlight {
      color: #0be76ece;
      font-weight: 500;
    }
    
    .button {
      display: inline-block;
      margin: 25px 10px 10px;
      padding: 14px 28px;
      background: linear-gradient(90deg, #0be76ece, #00cc66);
      color: black;
      font-weight: bold;
      border-radius: 50px;
      text-decoration: none;
      font-size: 16px;
      font-family: 'Orbitron', sans-serif;
      letter-spacing: 1px;
      transition: all 0.3s;
      border: none;
      box-shadow: 0 4px 15px rgba(0, 255, 0, 0.4);
    }
    
    .button:hover {
      background: linear-gradient(90deg, #00cc66, #00cc66);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 255, 0, 0.5);
    }
    
    .track-list, .prize-list, .benefit-list, .sponsor-list {
      list-style: none;
      padding-left: 10px;
      margin: 20px 0;
    }
    
    .track-list li, .prize-list li, .benefit-list li, .sponsor-list li {
      padding: 10px 15px;
      margin-bottom: 8px;
      background: rgba(0, 255, 0, 0.05);
      border-left: 3px solid #0be76ece;
      border-radius: 3px;
      color: #c0c0c0;
    }
    
    .track-list li:hover, .prize-list li:hover, .benefit-list li:hover, .sponsor-list li:hover {
      background: rgba(0, 255, 0, 0.1);
    }
    
    .track-icon, .prize-icon, .benefit-icon, .sponsor-icon {
      color: #0be76ece;
      margin-right: 10px;
      width: 20px;
      display: inline-block;
      text-align: center;
    }
    
    .event-details {
      background: rgba(0, 255, 0, 0.05);
      border-radius: 10px;
      padding: 20px;
      margin: 25px 0;
      border: 1px solid rgba(0, 255, 0, 0.2);
    }
    
    .event-details p {
      margin: 10px 0;
    }
    
    .social-links {
      margin-top: 30px;
      display: flex;
      justify-content: center;
      gap: 15px;
    }
    
    .social-links a:hover {
      background: rgba(0, 255, 0, 0.2);
      transform: translateY(-3px);
    }

    .whatsapp-share {
      background: linear-gradient(90deg, #25d366, #128C7E) !important;
      color: white !important;
    }
    
    .whatsapp-button {
      display: inline-block;
      margin: 25px 10px 10px;
      padding: 14px 28px;
      background: linear-gradient(90deg, #25d366, #128C7E);
      color: white;
      font-weight: bold;
      border-radius: 50px;
      text-decoration: none;
      font-size: 16px;
      font-family: 'Orbitron', sans-serif;
      letter-spacing: 1px;
      transition: all 0.3s;
      border: none;
      box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
    }
    
    .whatsapp-button:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 211, 102, 0.5);
    }

    .section {
      margin: 40px 0;
    }
    
    .footer {
      text-align: center;
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid rgba(0, 255, 0, 0.3);
      color: #888;
    }
    
    .footer strong {
      color: #0be76ece;
    }
    
    .cta-section {
      text-align: center;
      margin: 40px 0;
    }
    
    .special-award {
      background: linear-gradient(90deg, rgba(0, 255, 0, 0.05), rgba(0, 255, 0, 0.1));
      border-radius: 10px;
      padding: 15px;
      margin-top: 20px;
    }
    
    .special-award ul {
      margin-bottom: 0;
    }
    
    @media (max-width: 768px) {
      .container {
        padding: 20px;
        margin: 10px;
      }
      
      .button, .whatsapp-button {
        display: block;
        margin: 15px auto;
        width: 80%;
      }
    }

    .invitation-box {
      background: linear-gradient(135deg, rgba(0, 255, 0, 0.05) 0%, rgba(0, 255, 0, 0.1) 100%);
      border-radius: 15px;
      padding: 10px;
      margin: 40px auto;
      position: relative;
      max-width: 600px;
      overflow: hidden;
      border: 1px solid rgba(0, 255, 0, 0.2);
    }

    .pulse-border {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      border: 2px solid rgba(0, 255, 0, 0.3);
      border-radius: 15px;
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.02); opacity: 0.5; }
      100% { transform: scale(1); opacity: 1; }
    }

    .invitation-icon {
      font-size: 2.5rem;
      color: #0be76ece;
      margin-bottom: 20px;
      display: block;
      text-align: center;
    }

    .invitation-title {
      font-family: 'Orbitron', sans-serif;
      color: #0be76ece;
      text-align: center;
      font-size: 1.8rem;
      margin-bottom: 20px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    .invitation-text {
      text-align: center;
      color: #d0f0c0;
      font-size: 1.1rem;
      margin-bottom: 25px;
    }

    .invitation-features {
      list-style: none;
      padding: 0;
      margin: 0 0 30px 0;
    }

    .invitation-features li {
      color: #c0c0c0;
      margin: 12px 0;
      padding-left: 30px;
      position: relative;
      font-size: 1.1rem;
      transition: transform 0.3s ease;
    }

    .invitation-features li:hover {
      transform: translateX(10px);
      color: #d0f0c0;
    }

    .invitation-features li i {
      position: absolute;
      left: 0;
      color: #0be76ece;
      font-size: 1rem;
    }

    .invitation-cta {
      text-align: center;
    }

    .invitation-button {
      background: linear-gradient(90deg, #0be76ece, #00cc66);
      padding: 15px 40px;
      font-size: 1.1rem;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    .invitation-button:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 25px rgba(87, 233, 124, 0.4);
    }

    @media (max-width: 768px) {
      .invitation-box {
        margin: 20px 10px;
        padding: 20px;
      }
      
      .invitation-title {
        font-size: 1.5rem;
      }
      
      .invitation-features li {
        font-size: 1rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1 class="logo"> PBCTF 4.0</h1>
    </div>
    <div style="text-align: center;">
    <a href="https://pointblank.club/pbctf"><img src="https://i.ibb.co/WvLXqBDJ/pbctf.jpg" alt="pbctf" height="800px"/></a>
    </div>
    <div class="section">
    <h2>About PBCTF 4.0</h2>
    <p><strong class="highlight">Point Blank</strong> is back with the latest edition of Offline Capture The Flag event <strong class="highlight">PBCTF 4.0.</strong></p>
    <p>What started as a campus-wide CTF is now gearing up to become one of <b>Bangalore's biggest CTFs</b>, bringing together cybersecurity enthusiasts, ethical hackers, and problem-solvers from all across the region.</p>
    </div>

    <div class="section">
        <h2>CTF Categories</h2>
        <ul class="track-list">
          <li>🔐 Cryptography</li>
          <li>🕵 Forensics</li>
          <li>🔁 Reverse Engineering</li>
          <li>🌐 Web Application Security</li>
          <li>📱 Mobile App Security
          <li>☁ Cloud Security</li>
          <li>🌍 OSINT (Open Source Intelligence)</li>
        </ul>
      </div>

    <div class="event-details">
      <p><strong class="highlight">Event Date:</strong> 2nd August 2025</p>
      <p><strong class="highlight">Venue:</strong> CSE Block, Dayananda Sagar College of Engineering, Bengaluru</p>
      <p><strong class="highlight">Mode:</strong> Offline</p>
      <p><strong class="highlight">Team Size:</strong> Solo/Duo</p>
    </div>

    <div class="section">
      <h2>🏆 Prize Pool</h2>
      <ul class="prize-list">
        <li>💰Cash prizes for the Top 3 Teams</li>
        <li>🎓 Exclusive certification vouchers for the Top Performing Team</li>
      </ul>

    <div class="cta-section">
      <a href="https://pointblank.club/pbctf" class="button" style="color: #000000;">REGISTER NOW</a>
    </div>

    <div class="invitation-box">
      <div class="pulse-border"></div>
      <p class="invitation-text">Bring your team, bring your skills, and bring the heat. See you at the battlefield!</p>
    </div>
    <div class="cta-section">
    <a style="color: #ffffff;" href="https://wa.me/?text=PBCTF%204.0%20%E2%80%93%20Capture%20The%20Flag%20Competition%0A%0APoint%20Blank%20is%20back%20with%20PBCTF%204.0%2C%20an%20exciting%20offline%20CTF%20event.%0A%0AWhat%20started%20as%20a%20campus-wide%20event%20is%20now%20becoming%20one%20of%20Bangalore's%20biggest%20CTFs%20%E2%80%94%20uniting%20cybersecurity%20enthusiasts%2C%20ethical%20hackers%2C%20and%20problem-solvers%20from%20all%20over%20the%20region.%0A%0ACTF%20Categories%3A%0A-%20Cryptography%0A-%20Forensics%0A-%20Reverse%20Engineering%0A-%20Web%20Application%20Security%0A-%20Mobile%20App%20Security%0A-%20Cloud%20Security%0A-%20OSINT%20(Open%20Source%20Intelligence)%0A%0AEvent%20Details%3A%0ADate%3A%202nd%20August%202025%20%20%0AVenue%3A%20CSE%20Block%2C%20Dayananda%20Sagar%20College%20of%20Engineering%2C%20Bengaluru%20%20%0AMode%3A%20Offline%20%20%0ATeam%20Size%3A%20Solo%20or%20Duo%0A%0APrize%20Pool%3A%0A-%20Cash%20prizes%20for%20the%20Top%203%20Teams%20%20%0A-%20Certification%20vouchers%20for%20Top%20Performing%20Team%0A%0ABring%20your%20team%2C%20bring%20your%20skills%2C%20and%20bring%20the%20heat.%20See%20you%20at%20the%20battlefield.%0A%0ARegister%20now%3A%20https%3A%2F%2Fpointblank.club%2Fpbctf%20%0A%0AWarm%20Regards%2C%0ATeam%20Point%20Blank%0A%0AFollow%20us%3A%20%0ALinkedIn%3A%20https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fpoint-blank-d%2Fposts%2F%20%0AInstagram%3A%20https%3A%2F%2Fwww.instagram.com%2Fpointblank_dsce%2F" class="whatsapp-button" style="color: white !important; text-decoration: none;"><img src="https://static.vecteezy.com/system/resources/thumbnails/016/716/480/small/whatsapp-icon-free-png.png" style="height: 1.5em; vertical-align: middle; margin-right: 5px;" /> SHARE ON WHATSAPP</a>
    <p style="margin-top: 15px; text-align: center; font-size: 14px;">Invite students to participate and gain valuable exposure and real-world experience in cyber security. </p>
    </div>

    <div class="footer">
      <p>Warm Regards,<br><strong>Team Point Blank</strong></p>
    </div>

    <div style="text-align: center; margin-top: 20px;">
      <a href="https://www.linkedin.com/company/point-blank-d/posts/" target="_blank" style="color: white; text-decoration: none;">LinkedIn</a> <span> | </span>
      <a href="https://www.instagram.com/pointblank_dsce/" target="_blank" style="color: white; text-decoration: none;">Instagram</a> 
    </div>
   </div>
   </div>
</body>
</html>
"""

recipient_emails = ["saniya200631@gmail.com"]

# recipient_emails = [
# "principal@jssateb.ac.in", "principalubdt@gmail.com", "hvbyregowda@gmail.com", "principal@kssem.edu.in", "principal@sjce.ac.in",
# "principal@cmrit.ac.in", "principalmrit15@gmail.com", "dir.soa.hms@gmail.com", "principal@sahyadri.edu.in", "principal@atria.edu",
# "principal@rvce.edu.in", "bnmitprincipal@gmail.com", "principal@bnmit.in", "principalrymec@gmail.com", "principal@rymec.in",
# "principal@ewit.edu.in", "principal@navkisce.ac.in", "veeresh1971@gmail.com", "principalamruta@gmail.com", "director@cittumkur.org",
# "sureshtumkur@yahoo.com", "principal@vemanait.edu.in", "principal@git.edu", "keerthiresearch@yahoo.com", "narayana.bv73@gmail.com",
# "principalmmct@cmc.ac.in", "thippeswamy@vtu.ac.in", "shreedharkolekar@gmail.com", "guru14swamy@gmail.com", "aswathmu@gmail.com",
# "dbit.principal@gmail.com", "ppl-dsce@dayanandasagar.edu", "vsramamurthy@yahoo.com", "director@nittesoa.ac.in", "director_nittesoa@nitte.edu.in",
# "principal@rrce.org", "ytk_gowda@yahoo.com", "principal@newhorizonindia.edu", "principal@veerappanistyecs.org", "gecramatal@gmail.com",
# "principal@pes.edu", "santhoshkumarg@ewce.edu.in", "principal@vvce.ac.in", "suriakls@gmail.com", "principal@sjbit.edu.in",
# "principal@mitkundapura.com", "becprincipal@yahoo.com", "principaldrsmce@gmail.com", "principal@kittiptur.ac.in", "gttcpgmys@gmail.com",
# "anita.dpal@gmail.com", "principal@sode-edu.in", "pplgeckrpet2018@gmail.com", "principal.kitm@gmail.com", "principal.rvca@rvei.edu.in",
# "ndg0021@gmail.com", "shanthalageck@gmail.com", "principalkct@rediffmail.com", "zakirsab@gmail.com", "principal@klecet.edu.in",
# "principal.nit@navodaya.edu.in", "director@isab.in", "meenakshirpatil@gmail.com", "MSATHYA15@gmail.com", "sheerazzaidi@hotmail.com",
# "kgchandrashekar@yahoo.com", "principalait@acharya.ac.in", "principal@pdit.ac.in", "principal.apsce@gmail.com", "r.nagaraja@yahoo.com",
# "principal@drttit.edu.in", "principal.ksit@gmail.com", "ajenggcollege@gmail.com", "sskul@pes.edu", "principal@hsit.ac.in",
# "principal@bce.org.in", "director.asa2016@gmail.com", "principal@beads.edu.in", "ravishankarmcn@gmail.com", "principal@yit.edu.in",
# "principal@bitm.edu.in", "principal@ncetmail.com", "principal@saividya.ac.in", "principalbarch@gsss.edu.in", "principal@rljit.in",
# "principal@sgbit.edu.in", "principal@bgscet.ac.in", "mmbenal@gmail.com", "principal@gmit.ac.in", "kalpana_manchali123@yahoo.com",
# "prashanthbanakar77@gmail.com", "praveena.gowda@gmail.com", "dsk.bce@gmail.com", "mahe_awati@yahoo.com", "principal@nie.ac.in",
# "gcemprincipal@gmail.com", "gsapprincipal@gopalancolleges.com", "gcemprincipal@gopalancolleges.com", "nsriram3999@gmail.com",
# "principal@mcehassan.ac.in", "principal@pdaengg.com", "principal.rvitm@rvei.edu.in", "mvlatte@rediffmail.com", "principal@sit.ac.in",
# "principal@wcfa.ac.in", "principalaiet08@gmail.com", "engprincipal@theoxford.edu", "principal@mitmysore.in", "principal@sdmit.in",
# "principal@btibangalore.org", "drsaleembti@gmail.com", "bmssa.office@gmail.com", "principalsvgi@gmail.com", "coorgcitprincipal@gmail.com",
# "principal@dsatm.edu.in", "principal@gsss.edu.in", "aaad.archi@gmail.com", "sreeramareddy90@gmail.com", "ctjayadeva@yahoo.com",
# "gtraju1990@yahoo.com", "principal@sjec.ac.in", "principal@mmec.edu.in", "principal.gecch@gmail.com", "bshivakumara@gmail.com",
# "rkcivil2008@gmail.com", "narayanbyrappa53@gmail.com", "principal.ait.t@gmail.com", "anami_basu@hotmail.com", "mushtaqbhavikatti@yahoo.com",
# "basavaraj971@gmail.com", "principal@sapthagiri.edu.in", "principal@bitmangalore.edu.in", "suresha_rec@rediffmail.com",
# "director.bmsarch@gmail.com", "principal@hkbk.edu.in", "dean@sjbsap.edu.in", "sasi_mun@rediffmail.com", "mahendrakv@gmail.com",
# "hpjagga@gmail.com", "principal@jnnce.ac.in", "channu2k3@yahoo.com", "ramismk@pace.edu.in", "principal@rgit.ac.in",
# "gundannavarganesh1@gmail.com", "principal@sjcit.ac.in", "principal@rvca.in", "acs.exam@gmail.com", "msvgi@yahoo.com",
# "deanbgssap.edu.in", "2014bgssap@gmail.com", "principal@kssa.edu.in", "principalengg@mvjce.edu.in", "principal@msa.edu.in",
# "pplgect@gmail.com", "shravankerur@yahoo.com", "principal@jainbgm.in", "principal@drait.edu.in", "vasthu.arch@gmail.com",
# "sditprincipal@gmail.com", "tjitprincipal@tjohngroup.com", "gpkbms@gmail.com", "principal@shrideviengineering.org",
# "principal@sjmit.ac.in", "principaljvit@gmail.com", "principal@sirmvit.edu", "nvrnaidu@gmail.com","principal@rnsit.ac.in","pro@gcu.edu.in","info@jyothyit.ac.in", "principal@sit.ac.in","info@sirmvit.edu", "admn@msrit.edu","principal@msrit.edu", "principal@dsatm.edu.in", "facility-head@dsatm.edu.in","hodaiml@dsatm.edu.in","hod-csd@dsatm.edu.in","deanacademics@dsatm.edu.in", "hod.eee@dsatm.edu.in", "hodise@dsatm.edu.in","provc@reva.edu.in","info@reva.edu.in","hod-me@dayanandasagar.edu","hod-rai@dayanandasagar.edu","hod-ise@dayanandasagar.edu","hod-eee@dayanandasagar.edu","hod-csd@dayanandasagar.edu","hod-csds@dayanandasagar.edu","hod-cse@dayanandasagar.edu"
# ]

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(USERNAME, PASSWORD)

    for i,email in enumerate(recipient_emails):
        try:
            message = MIMEMultipart()
            message["From"] = USERNAME
            message["To"] = email
            message["Subject"] = SUBJECT
            
            message.attach(MIMEText(html_content, "html"))
            
            server.sendmail(USERNAME, email, message.as_string())
            print(f"{i}. Email sent to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {e}")
print("All emails sent successfully!")