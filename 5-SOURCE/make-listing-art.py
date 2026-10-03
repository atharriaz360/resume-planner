from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
W=Path(__file__).resolve().parent/"renders"
W.mkdir(exist_ok=True)
BG='#f8fafc';INK='#172554';INDIGO='#4f46e5';TEAL='#0f766e';MUTED='#475569';LINE='#dbe2ed'
style=ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=13,textColor=colors.HexColor(MUTED))
def para(c,text,x,y,w,size=9,color=MUTED,bold=False):
 st=ParagraphStyle('x',parent=style,fontSize=size,leading=size*1.45,textColor=colors.HexColor(color),fontName='Helvetica-Bold' if bold else 'Helvetica');p=Paragraph(text,st);_,h=p.wrap(w,900);p.drawOn(c,x,y-h);return h
def box(c,x,y,w,h,title,text):
 c.setFillColor(colors.white);c.setStrokeColor(colors.HexColor(LINE));c.roundRect(x,y-h,w,h,12,fill=1,stroke=1);para(c,title,x+14,y-13,w-28,12,TEAL,True);para(c,text,x+14,y-39,w-28)
slides=[
('Resume Builder + Job Tracker','Career Hub browser app','Build your professional record. Choose resume content. Track application stages.','Two resume layouts | PDF via browser print','01-hero-resume-builder'),
('Two resume layouts','Choose the structure for your content','Executive: single column. Mint Modern: two columns with seven accent choices.','Review the saved PDF before applying.','02-two-templates'),
('Choose your workspace look','Light, dark, and colour controls','Five app accents: Indigo, Emerald, Amber, Rose, Slate. Focus mode and a sticky header.','Responsive layout | Browser app','03-colours-dark-mobile'),
('Keep your next step in view','Hub dashboard','See application counts, upcoming application follow-ups, and a suggested next step.','Readiness measures setup completion.','04-hub-dashboard'),
('Organise your applications','Five recorded stages','Wishlist / Applied / Interviewing / Offer / Rejected. Keep salary notes, contact details, and follow-up dates.','Applications are submitted outside the app.','05-job-tracker'),
('Prepare with clear examples','Your career playbook','12 Golden Rules plus guides on achievements, interview stories, networking, and reviewing offers.','Add your own notes. Adapt advice to the role.','06-playbook-guide'),
('For your next career move','Students, job seekers, professionals','Include study projects and volunteering. Track opportunities. Reuse relevant work achievements.','Use your own facts and experience.','07-for-students-jobhunters-pros'),
('Your experience, clearly presented','Resume preview and PDF export','Choose the details to include. Open browser printing. Save and review your PDF.','Long content can span multiple pages.','08-full-resume-view'),
('Start with three useful steps','Add / Build / Track','1. Add your experience. 2. Build a resume. 3. Apply outside the app and track your progress.','Export a JSON backup after important changes.','09-how-it-works'),
('Your career search workspace','What your download contains','Career-Hub.html / Career-Hub-Start-Here.pdf / LICENSE.txt','Digital download | Personal & household use','10-everything-included')]
c=canvas.Canvas(str(W/'listing-native.pdf'),pagesize=(1000,800))
for title,sub,body,foot,name in slides:
 c.setFillColor(colors.HexColor(BG));c.rect(0,0,1000,800,fill=1,stroke=0)
 c.setFillColor(colors.HexColor(INDIGO));c.roundRect(65,675,150,40,12,fill=1,stroke=0);para(c,'CAREER HUB',80,704,130,13,'#ffffff',True)
 para(c,title,65,623,870,44,INK,True);para(c,sub,65,485,870,22,TEAL,True)
 c.setFillColor(colors.white);c.setStrokeColor(colors.HexColor(LINE));c.roundRect(65,190,870,240,22,fill=1,stroke=1);para(c,body,98,390,804,27,MUTED)
 para(c,foot,65,145,870,17,INDIGO,True);para(c,'BROWSER APP  /  DIGITAL DOWNLOAD  /  NO PHYSICAL ITEM',65,90,870,13,MUTED)
 c.showPage()
c.save()
