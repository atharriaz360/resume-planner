from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
R=Path(__file__).resolve().parents[1]
BG='#f8fafc';INK='#172554';INDIGO='#4f46e5';TEAL='#0f766e';MUTED='#475569';LINE='#dbe2ed'
style=ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=13,textColor=colors.HexColor(MUTED))
def para(c,text,x,y,w,size=9,color=MUTED,bold=False):
 st=ParagraphStyle('x',parent=style,fontSize=size,leading=size*1.45,textColor=colors.HexColor(color),fontName='Helvetica-Bold' if bold else 'Helvetica');p=Paragraph(text,st);_,h=p.wrap(w,900);p.drawOn(c,x,y-h);return h
def box(c,x,y,w,h,title,text):
 c.setFillColor(colors.white);c.setStrokeColor(colors.HexColor(LINE));c.roundRect(x,y-h,w,h,12,fill=1,stroke=1);para(c,title,x+14,y-13,w-28,12,TEAL,True);para(c,text,x+14,y-39,w-28)
def base(c,page):
 c.setFillColor(colors.HexColor(BG));c.rect(0,0,595,842,fill=1,stroke=0);c.setFillColor(colors.HexColor(INDIGO));c.roundRect(40,760,34,34,9,fill=1,stroke=0);c.setStrokeColor(colors.white);c.setLineWidth(2)
 for y,end in [(784,65),(777,61),(770,65)]:c.line(49,y,end,y)
 para(c,'Career Hub',85,792,460,22,INK,True);para(c,'RESUME BUILDER &amp; JOB SEARCH TRACKER',85,766,460,8,INDIGO)
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor(MUTED));c.drawString(40,24,'Career Hub | DigiDesignLab1 | Start Here');c.drawRightString(555,24,f'Page {page} of 2')
def make_guide(out):
 c=canvas.Canvas(str(out),pagesize=(595,842));c.setTitle('Career Hub - Start Here');c.setAuthor('DigiDesignLab1');base(c,1)
 para(c,'Welcome to your career workspace.',40,732,515,22,INK,True);para(c,'Keep your experience, applications, and preparation together. Choose the downloaded app or the website to get started.',40,696,515,10)
 box(c,40,648,251,147,'On your computer','1. Unzip Career-Hub.zip into a folder you will keep.<br/>2. Open Career-Hub.html in a browser.<br/>3. Read the guide, then try Settings &gt; Load sample data.<br/>4. Exit sample mode before entering your own information.')
 box(c,304,648,251,147,'On your phone or tablet','1. Open the website in your browser.<br/>2. Use the same browser for saved entries.<br/>3. The layout adapts to the screen; local HTML access and PDF printing vary by device.<br/>A computer is recommended for initial setup and PDFs.')
 box(c,40,486,515,85,'YOUR APP WEBSITE','<link href="https://resume-planner-rouge.vercel.app/" color="#4f46e5">https://resume-planner-rouge.vercel.app/</link><br/>This is a public website, not a private account link. Online and downloaded copies have separate browser storage; transfer data using JSON backup/restore.')
 box(c,40,387,515,174,'Your first steps','1. <b>Experience Bank:</b> save your Profile, then add relevant roles, projects, education, certifications, and skills.<br/>2. <b>Resume Builder:</b> choose Executive or Mint Modern and select your content.<br/>3. <b>Job Tracker:</b> record an opportunity and its status, dates, salary notes, and next follow-up.<br/>4. <b>Contacts:</b> record useful conversation details and a next-contact date.<br/>5. <b>Playbook:</b> read the short guides and add your own preparation notes.')
 box(c,40,199,515,132,'Keep a backup of your workspace','Your entries are stored in your browser. Clearing storage, private browsing, or using another browser/device/file location may make entries unavailable.<br/><br/>Use Settings &gt; Export backup after important changes. Restore backup replaces the destination workspace, so export its existing data first. Keep JSON files somewhere you trust. Resume PDFs are not workspace backups.')
 c.showPage();base(c,2);para(c,'Good to know',40,732,515,23,INK,True)
 box(c,40,689,251,251,'What is included','<b>Hub:</b> counts, application follow-ups, setup checklist, and a suggested next action.<br/><br/><b>Experience Bank:</b> profile and professional record.<br/><br/><b>Resume Builder:</b> two layouts; Mint Modern has seven accents.<br/><br/><b>Job Tracker &amp; Contacts:</b> application stages and conversation notes.<br/><br/><b>Playbook:</b> 12 Golden Rules and practical preparation guides.<br/><br/><b>Appearance:</b> light/dark, five app accents, focus mode, sticky header.')
 box(c,304,689,251,251,'Save a resume as PDF','Open Resume Builder and use <b>Save as PDF</b>. In the browser print dialog:<br/><br/>1. Choose Save as PDF or the system PDF option.<br/>2. Use 100% scale.<br/>3. Turn Headers and footers off.<br/>4. Enable Background graphics for colours.<br/>5. If Margins is offered, choose None.<br/><br/>Review every saved page. Long content may span pages. Follow the employer\'s format requirements. Word export is not included.')
 box(c,40,424,251,151,'Troubleshooting','<b>Missing entries?</b> Check the original browser and app location, then restore a JSON backup if available.<br/><br/><b>New device?</b> Export on the old device and restore on the new one.<br/><br/><b>PDF looks different?</b> Check print settings or try a current desktop browser.')
 box(c,304,424,251,151,'Use the tools thoughtfully','Readiness counts completed setup steps, not hiring chances.<br/><br/>Follow-up dates are in-app prompts, not alerts. Review email drafts and send them in your own email app.<br/><br/>No automatic applying or cloud sync.')
 box(c,40,259,515,91,'Your download & licence','Career-Hub.html + Career-Hub-Start-Here.pdf + LICENSE.txt.<br/>Personal and household use on your own devices. No resale or redistribution outside your household. See LICENSE.txt for full terms.')
 box(c,40,154,515,88,'Thank you','Need help? Message DigiDesignLab1 through Etsy with your device, browser, and the step that caused trouble. Leave out sensitive personal information.<br/>An optional, honest review can describe your experience using Career Hub.')
 c.save()
make_guide(R/"1-SELL-THIS/Career-Hub-Start-Here.pdf")
