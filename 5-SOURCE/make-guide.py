from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
R=Path(__file__).resolve().parents[1]
BG='#faf9f6';INK='#172239';INDIGO='#375875';TEAL='#0b7c73';MUTED='#475569';LINE='#dbe2ed'
style=ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=13,textColor=colors.HexColor(MUTED))
def para(c,text,x,y,w,size=9,color=MUTED,bold=False):
 st=ParagraphStyle('x',parent=style,fontSize=size,leading=size*1.45,textColor=colors.HexColor(color),fontName='Helvetica-Bold' if bold else 'Helvetica');p=Paragraph(text,st);_,h=p.wrap(w,900);p.drawOn(c,x,y-h);return h
def box(c,x,y,w,h,title,text):
 c.setFillColor(colors.white);c.setStrokeColor(colors.HexColor(LINE));c.setLineWidth(.6);c.roundRect(x,y-h,w,h,10,fill=1,stroke=1);para(c,title,x+14,y-13,w-28,12,TEAL,True);used=para(c,text,x+14,y-39,w-28);assert used <= h-45, f'Card overflows: {title} ({used} > {h-45})'
def base(c,page):
 c.setFillColor(colors.HexColor(BG));c.rect(0,0,595,842,fill=1,stroke=0);c.setFillColor(colors.HexColor(INDIGO));c.roundRect(40,760,34,34,9,fill=1,stroke=0);c.setStrokeColor(colors.white);c.setLineWidth(2)
 for y,end in [(784,65),(777,61),(770,65)]:c.line(49,y,end,y)
 para(c,'Career Hub',85,792,460,22,INK,True);para(c,'RESUME BUILDER &amp; JOB SEARCH TRACKER',85,766,460,8,INDIGO)
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor(MUTED));c.drawString(40,24,'Career Hub | KaelLabs | Start Here');c.drawRightString(555,24,f'Page {page} of 2')
def make_guide(out):
 c=canvas.Canvas(str(out),pagesize=(595,842));c.setTitle('Career Hub - Start Here');c.setAuthor('KaelLabs');base(c,1)
 para(c,'Welcome to your career workspace.',40,732,515,22,INK,True);para(c,'Keep your experience, applications, and preparation together. A calm space for your next application. Start with your downloaded app.',40,696,515,10)
 box(c,40,648,251,147,'On your computer','1. Unzip Career-Hub.zip into a folder you will keep.<br/>2. Open Career-Hub.html in a browser.<br/>3. Read the guide, then try Settings &gt; Load demo data.<br/>4. Edit the examples, or use Remove all data to start fresh. Demo edits stay after refresh.')
 box(c,304,648,251,147,'On your phone or tablet','1. Open the website in your browser.<br/>2. Use the same browser for saved entries.<br/>3. The layout adapts to the screen; local HTML access and PDF printing vary by device.<br/>A computer is recommended for initial setup and PDFs.')
 box(c,40,486,515,85,'YOUR DOCUMENT WORKSPACE','Open Resume Builder or Cover Letter to enter the full editing workspace automatically. Templates and Style are on the left; Review and Sections or Letter are on the right. Use Job Tracker to return to your applications.')
 box(c,40,387,515,174,'Your first steps','1. <b>Experience Bank:</b> save your Profile, then add relevant roles, projects, education, certifications, skills, and awards.<br/>2. <b>Resume Builder:</b> choose a design, refine Style, then use Sections to show, hide and arrange content.<br/>3. <b>Job Tracker:</b> record an opportunity and its status, dates, salary notes, and next follow-up.<br/>4. <b>Contacts:</b> record useful conversation details and a next-contact date.<br/>5. <b>Cover Letter:</b> add a recipient and your own letter; save as PDF.<br/>6. <b>Playbook:</b> read the guides and add preparation notes.')
 box(c,40,199,515,132,'Keep a backup of your workspace','Your entries are stored in your browser. Clearing storage, private browsing, or using another browser/device/file location may make entries unavailable.<br/><br/>Use Settings &gt; Export backup after important changes. Restore backup replaces the destination workspace, so export its existing data first. Keep JSON files somewhere you trust. Resume PDFs are not workspace backups.')
 c.showPage();base(c,2);para(c,'Good to know',40,732,515,23,INK,True)
 box(c,40,689,251,251,'What is included','<b>Hub:</b> counts, application follow-ups, setup checklist, and a suggested next action.<br/><b>Experience Bank:</b> profile and professional record.<br/><b>Resume Builder:</b> 24 template styles (3 layouts × 4 colours × 2 header styles), section ordering, font choices, adjustable sizes, A4/US Letter, and on-device review checks.<br/><b>Job Tracker &amp; Contacts:</b> application stages and conversation notes.<br/><b>Playbook:</b> 12 Golden Rules and practical preparation guides.<br/><b>Cover Letter:</b> editable draft, job details, and PDF export.')
 box(c,304,689,251,251,'Save a resume or letter as PDF','Open Resume Builder or Cover Letter and use <b>Download PDF</b>. In the browser print dialog:<br/><br/>1. Choose Save as PDF or the system PDF option.<br/>2. Use 100% scale.<br/>3. Turn Headers and footers off.<br/>4. Enable Background graphics for colours.<br/>5. If Margins is offered, choose None.<br/><br/>Review every saved page. Long content may span pages. Follow the employer\'s format requirements. Word export is not included.')
 box(c,40,424,251,151,'Troubleshooting','<b>Missing entries?</b> Check the original browser and app location, then restore a JSON backup if available.<br/><b>New device?</b> Export on the old device and restore on the new one.<br/><b>PDF looks different?</b> Check print settings or try a current desktop browser.')
 box(c,304,424,251,151,'Use the tools thoughtfully','Completion counts filled details. Review checks formatting and content, not ATS approval or hiring chances.<br/><br/>Follow-up dates are in-app prompts, not alerts. Review email drafts and send them in your own email app.<br/><br/>No automatic applying or cloud sync.')
 box(c,40,259,515,86,'Your download & licence','Career-Hub.html + Career-Hub-Start-Here.pdf + LICENSE.txt.<br/>Personal and household use on your own devices. No resale or redistribution outside your household. See LICENSE.txt for full terms.')
 c.setFillColor(colors.HexColor(INDIGO));c.roundRect(40,40,515,128,12,fill=1,stroke=0)
 para(c,'Thank you for choosing Career Hub. It truly means a lot.',56,154,483,16,'#ffffff',True)
 para(c,'Your experience matters. Make it clear, keep it organised, and take your next step with care.<br/>Need help? Message <b>KaelLabs on Etsy</b>: device + browser + exact step. Leave out private career details.',56,122,483,9,'#ffffff')
 para(c,'If Career Hub helps you, a short honest review would mean the world and helps other job seekers find it. Reviews are optional; support is always here, whether you review or not.<br/>Planning more of life? Visit <b>KaelLabs on Etsy</b> for more calm, private, pay-once tools.',56,86,483,8.5,'#e7eef3')

 c.save()
import sys
make_guide(Path(sys.argv[1]) if len(sys.argv)>1 else R/"1-SELL-THIS/Career-Hub-Start-Here.pdf")
