import requests
import datetime

today = datetime.date.today()
results = []
results.append(f"KARTIK MELKANI — MASTER SPONSORSHIP JOB MONITOR — {today}\n")
results.append(f"NCNZ APC: 367690 | AHPRA: NMW0004061692\n")
results.append(f"Delhi, India | +91 9410965768 | kartikmelkani123@gmail.com\n")
results.append("="*60 + "\n\n")
results.append("HOW TO USE:\n")
results.append("1. Open EACH link in Chrome\n")
results.append("2. Search for HCA / RN / Care Worker jobs\n")
results.append("3. NZ jobs → attach NZ CV + NZ Cover Letter\n")
results.append("4. AU jobs → attach AU CV + AU Cover Letter\n")
results.append("5. Apply directly — no middleman!\n\n")
results.append("="*60 + "\n\n")

# ══════════════════════════════════════════════════════════
# SECTION 1 — NZ HOSPITALS (AEWV / GREEN LIST SPONSORS)
# ══════════════════════════════════════════════════════════

NZ_HOSPITALS = [

    # ── REMOTE / RURAL — HIGHEST PRIORITY ─────────────────
    # These are most desperate — most likely to sponsor YOU

    ("★ Kaitaia Hospital — Far North NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=kaitaia"),

    ("★ Rawene Hospital — Hokianga NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=rawene"),

    ("★ Dargaville Hospital — Northland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=dargaville"),

    ("★ Bay of Islands Hospital — Northland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=bay+of+islands"),

    ("★ Grey Base Hospital — West Coast NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=greymouth"),

    ("★ Buller Health Westport — West Coast NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=westport"),

    ("★ Hokitika Hospital — West Coast NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=hokitika"),

    ("★ Gisborne Hospital — East Coast NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=gisborne"),

    ("★ Wairoa Hospital — Hawkes Bay NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=wairoa"),

    ("★ Taumarunui Hospital — King Country NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=taumarunui"),

    ("★ Te Kuiti Hospital — King Country NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=te+kuiti"),

    ("★ Taihape Community Hospital — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=taihape"),

    ("★ Dannevirke Community Hospital — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=dannevirke"),

    ("★ Te Anau Community Hospital — Fiordland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=te+anau"),

    ("★ Collingwood Area Health — Golden Bay NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=collingwood"),

    ("★ Takaka Health Centre — Golden Bay NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=takaka"),

    ("★ Opotiki Community Hospital — Eastern Bay NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=opotiki"),

    ("★ Murupara Health Centre — Bay of Plenty NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=murupara"),

    ("★ Stewart Island Health — Southland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=stewart+island"),

    ("★ Roxburgh Health Centre — Central Otago NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=roxburgh"),

    # ── NZ REGIONAL HOSPITALS ─────────────────────────────

    ("Whangarei Hospital — Northland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=whangarei"),

    ("Waikato Hospital — Hamilton NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=waikato"),

    ("Tauranga Hospital — Bay of Plenty NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=tauranga"),

    ("Rotorua Hospital — Bay of Plenty NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=rotorua"),

    ("Hawkes Bay Regional Hospital — Hastings NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=hawkes+bay"),

    ("Taranaki Base Hospital — New Plymouth NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=taranaki"),

    ("Whanganui Hospital — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=whanganui"),

    ("Palmerston North Hospital — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=palmerston+north"),

    ("Wellington Hospital — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=wellington"),

    ("Hutt Hospital — Lower Hutt NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=hutt"),

    ("Nelson Hospital — Top of South NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=nelson"),

    ("Wairau Hospital Blenheim — Marlborough NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=blenheim"),

    ("Timaru Hospital — South Canterbury NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=timaru"),

    ("Ashburton Hospital — Mid Canterbury NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=ashburton"),

    ("Christchurch Hospital — Canterbury NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=christchurch"),

    ("Dunedin Hospital — Otago NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=dunedin"),

    ("Southland Hospital Invercargill — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=invercargill"),

    ("Lakes District Hospital Queenstown — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=queenstown"),

    ("Dunstan Hospital Clyde — Central Otago NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=dunstan"),

    ("Oamaru Hospital — North Otago NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=oamaru"),

    ("Auckland City Hospital — NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=auckland"),

    ("Middlemore Hospital — South Auckland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=middlemore"),

    ("North Shore Hospital — Auckland NZ",
     "https://careers.tewhatuora.govt.nz/jobs?keywords=north+shore"),

    # ── NZ PRIVATE HOSPITALS ──────────────────────────────

    ("Mercy Ascot Hospital — Auckland NZ",
     "https://www.mercyascot.co.nz/about/careers/"),

    ("Southern Cross Hospitals — NZ Network",
     "https://www.southerncross.co.nz/group/careers"),

    ("Braemar Hospital — Hamilton NZ",
     "https://www.braemarhospital.co.nz/about/careers/"),

    ("Mercy Hospital Dunedin — NZ",
     "https://www.mercyhospital.org.nz/about/careers/"),

    # ── NZ AGED CARE — ACTIVE AEWV SPONSORS ──────────────

    ("★ Ryman Healthcare — All NZ (Best Sponsor!)",
     "https://rymanhealthcare.co.nz/careers/"),

    ("★ Oceania Care — All NZ",
     "https://www.oceania.co.nz/careers"),

    ("★ Summerset Group — All NZ",
     "https://www.summerset.co.nz/careers/"),

    ("★ Arvida Group — All NZ",
     "https://www.arvida.co.nz/careers/"),

    ("★ Metlifecare — All NZ",
     "https://www.metlifecare.co.nz/about-us/careers/"),

    ("★ Bupa Care Services NZ",
     "https://www.bupa.co.nz/about-bupa/careers"),

    ("★ Radius Care — All NZ",
     "https://www.radiuscare.co.nz/careers/"),

    ("★ Healthcare of NZ HCNZ",
     "https://www.healthcarenz.co.nz/careers"),

    ("★ Geneva Healthcare NZ",
     "https://www.genevahealth.com/careers"),

    ("CHT Care Homes — Auckland/Waikato",
     "https://www.cht.org.nz/careers/"),

    ("Elizabeth Knox Home Hospital — Auckland",
     "https://www.elizabethknox.org.nz/employment/"),

    ("Norfolk Court Home Hospital — Wellington",
     "https://www.norfolkcourt.org.nz/careers/"),

    ("Nurse Maude — Canterbury NZ",
     "https://www.nursemaude.org.nz/about-us/careers/"),

    ("Enliven NZ — South Island",
     "https://www.enliven.org.nz/careers/"),

    ("The Selwyn Foundation — Auckland",
     "https://www.selwyn.org.nz/careers/"),

    ("MercyHospice Auckland — NZ",
     "https://www.mercyhospice.org.nz/about/work-with-us/"),

    ("Presbyterian Support Otago — Dunedin",
     "https://www.psotago.org.nz/work-with-us/"),

    ("Methodist Mission Southern — Dunedin",
     "https://www.methodist.org.nz/jobs/"),

    ("Mercy Parklands — Christchurch",
     "https://www.mercyparklands.co.nz/careers/"),

    ("Right at Home NZ — Nationwide",
     "https://www.rightathome.co.nz/careers/"),

    ("Access Community Health NZ",
     "https://www.accesscommunityhealth.co.nz/careers/"),

    ("Green Cross Health NZ",
     "https://www.greencrosshealth.co.nz/careers"),

    # ── NZ DISABILITY SUPPORT ─────────────────────────────

    ("★ Spectrum Care NZ — AEWV Sponsor",
     "https://www.spectrumcare.org.nz/about-us/join-our-team/"),

    ("IHC New Zealand Disability",
     "https://www.ihc.org.nz/careers/"),

    ("CCS Disability Action NZ",
     "https://www.ccsdisabilityaction.org.nz/about-us/work-with-us/"),

    ("Emerge Aotearoa NZ",
     "https://www.emerge.org.nz/join-our-team/"),

    ("Community Care Trust Auckland",
     "https://www.communitycart.org.nz/join-us/"),

    ("Visions of a Helping Hand Canterbury",
     "https://www.visions.org.nz/about/vacancies/"),

    # ── NZ HOSPICE / PALLIATIVE ───────────────────────────

    ("Totara Hospice South Auckland",
     "https://www.totarahospice.org.nz/about-us/careers/"),

    ("Arohanui Hospice Palmerston North",
     "https://www.arohanuihospice.org.nz/careers/"),

    ("Te Omanga Hospice Wellington",
     "https://www.teomanga.org.nz/join-our-team/"),

    ("Cranford Hospice Hawkes Bay",
     "https://www.cranfordhospice.org.nz/careers/"),

    ("Otago Community Hospice Dunedin",
     "https://www.otagohospice.co.nz/careers/"),

    # ── NZ MAORI HEALTH ───────────────────────────────────

    ("The Fono Health Auckland",
     "https://www.thefono.org/careers/"),

    ("Tu Ora Compass Health Wellington",
     "https://www.tuora.org.nz/careers/"),

    # ── NZ RECRUITMENT AGENCIES ───────────────────────────

    ("★ Medacs Healthcare NZ — Best Agency",
     "https://apac.medacs.com/find-a-job/"),

    ("OneStaff Healthcare NZ",
     "https://www.onestaff.co.nz/"),

    ("Alpha Healthcare NZ",
     "https://www.alphahealthcare.co.nz/careers"),

    ("JPS Medical Recruitment NZ",
     "https://www.jpsmedical.com/nz/jobs/"),

]

# ══════════════════════════════════════════════════════════
# SECTION 2 — AUSTRALIA HOSPITALS (482/186 SPONSORS)
# ══════════════════════════════════════════════════════════

AU_HOSPITALS = [

    # ── NT — MOST LIKELY TO SPONSOR ───────────────────────

    ("★ Royal Darwin Hospital NT — 482/186",
     "https://jobs.nt.gov.au/search?query=registered+nurse"),

    ("★ Alice Springs Hospital NT — 482",
     "https://jobs.nt.gov.au/search?query=nurse+alice+springs"),

    ("★ Katherine District Hospital NT — 482",
     "https://jobs.nt.gov.au/search?query=nurse+katherine"),

    ("★ Tennant Creek Hospital NT — 482",
     "https://jobs.nt.gov.au/search?query=nurse+tennant+creek"),

    ("★ Palmerston Regional Hospital NT — 482/186",
     "https://jobs.nt.gov.au/search?query=registered+nurse+palmerston"),

    ("★ NT Health — All NT Nursing Jobs",
     "https://jobs.nt.gov.au/search?query=registered+nurse"),

    # ── TAS — SHORTAGE AREA ───────────────────────────────

    ("★ North West Regional Hospital Burnie TAS — 482/186",
     "https://www.ths.tas.gov.au/jobs?keywords=registered+nurse+burnie"),

    ("★ Launceston General Hospital TAS — 482/186",
     "https://www.ths.tas.gov.au/jobs?keywords=registered+nurse+launceston"),

    ("★ Mersey Community Hospital TAS — 482",
     "https://www.ths.tas.gov.au/jobs?keywords=nurse+mersey"),

    ("★ King Island District Hospital TAS — 482",
     "https://www.ths.tas.gov.au/jobs?keywords=nurse+king+island"),

    ("★ TAS Health — All Nursing Jobs",
     "https://www.ths.tas.gov.au/jobs"),

    ("★ Calvary Health Care TAS — 482/186",
     "https://www.calvarycare.org.au/careers/"),

    ("★ Respect Aged Care TAS — 482/186",
     "https://careers.respect.com.au/"),

    # ── WA WACHS — #1 EASIEST 482 IN AUSTRALIA ───────────

    ("★ Geraldton Regional Hospital WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Broome Regional Hospital WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Kalgoorlie Health Campus WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Albany Health Campus WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Port Hedland Health WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Karratha Health Campus WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Bunbury Regional Hospital WACHS WA — 482/186",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Derby Hospital WACHS WA — 482",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Carnarvon Hospital WACHS WA — 482",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ WA Health — All WACHS Jobs",
     "https://www.health.wa.gov.au/About-us/Careers"),

    ("★ Hall Prior Aged Care WA — 482/186",
     "https://www.hallandprior.com.au/careers/"),

    # ── QLD REMOTE ────────────────────────────────────────

    ("★ Mount Isa Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+mount+isa"),

    ("★ Mackay Base Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+mackay"),

    ("★ Cairns Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+cairns"),

    ("★ Townsville University Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+townsville"),

    ("★ Rockhampton Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+rockhampton"),

    ("★ Bundaberg Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+bundaberg"),

    ("★ Toowoomba Hospital QLD — 482/186",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+toowoomba"),

    ("★ Thursday Island Hospital QLD — 482",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+thursday+island"),

    ("★ Longreach Hospital QLD — 482",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+longreach"),

    ("★ Charleville Hospital QLD — 482",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=nurse+charleville"),

    ("★ QLD Health SmartJobs — All Nursing",
     "https://smartjobs.qld.gov.au/jobtools/jncustomsearch.jobsearch?in_keyword=registered+nurse"),

    # ── VIC REGIONAL ──────────────────────────────────────

    ("★ Mildura Base Public Hospital VIC — 482/186",
     "https://www.seek.com.au/jobs?keywords=mildura+hospital+nurse&daterange=30"),

    ("★ Wimmera Health Care Group Horsham VIC — 482/186",
     "https://www.whcg.org.au/careers/"),

    ("★ Goulburn Valley Health Shepparton VIC — 482/186",
     "https://www.gvhealth.org.au/careers/"),

    ("★ Bendigo Health VIC — 482/186",
     "https://www.bendigohealth.org.au/careers/"),

    ("★ Ballarat Health Services VIC — 482/186",
     "https://www.bhs.org.au/work-with-us/"),

    ("★ South West Healthcare Warrnambool VIC — 482/186",
     "https://www.swh.net.au/careers/"),

    ("★ Latrobe Regional Hospital VIC — 482/186",
     "https://www.lrh.com.au/careers/"),

    ("★ Albury Wodonga Health VIC — 482/186",
     "https://www.awh.org.au/careers/"),

    ("★ Echuca Regional Health VIC — 482/186",
     "https://www.echucahealth.org.au/careers/"),

    ("Northeast Health Wangaratta VIC — 482",
     "https://www.nhw.org.au/careers/"),

    ("West Gippsland Healthcare VIC — 482/186",
     "https://www.wghg.com.au/careers/"),

    ("Central Gippsland Health Sale VIC — 482",
     "https://www.cghs.com.au/careers/"),

    ("East Grampians Health Ararat VIC — 482",
     "https://www.eghs.net.au/careers/"),

    ("Swan Hill District Health VIC — 482",
     "https://www.shdh.org.au/careers/"),

    # ── NSW REGIONAL ──────────────────────────────────────

    ("★ Tamworth Rural Referral Hospital NSW — 482/186",
     "https://www.seek.com.au/jobs?keywords=tamworth+hospital+nurse&daterange=30"),

    ("★ Orange Health Service NSW — 482/186",
     "https://www.seek.com.au/jobs?keywords=orange+health+service+nurse&daterange=30"),

    ("★ Dubbo Health Service NSW — 482/186",
     "https://www.seek.com.au/jobs?keywords=dubbo+health+nurse&daterange=30"),

    ("★ Albury Base Hospital NSW — 482/186",
     "https://www.seek.com.au/jobs?keywords=albury+hospital+nurse&daterange=30"),

    ("★ Wagga Wagga Rural Referral NSW — 482/186",
     "https://www.seek.com.au/jobs?keywords=wagga+wagga+hospital+nurse&daterange=30"),

    ("★ Lismore Base Hospital NSW — 482/186",
     "https://www.seek.com.au/jobs?keywords=lismore+hospital+nurse&daterange=30"),

    ("★ Broken Hill Health Service NSW — 482",
     "https://www.seek.com.au/jobs?keywords=broken+hill+nurse+sponsorship&daterange=30"),

    ("★ NSW Health — All Regional Nursing",
     "https://www.seek.com.au/jobs?keywords=nsw+health+registered+nurse+regional+sponsorship&daterange=30"),

    # ── SA REGIONAL ───────────────────────────────────────

    ("★ Whyalla Hospital SA — 482/186",
     "https://sahealth.sa.gov.au/careers"),

    ("★ Port Augusta Hospital SA — 482/186",
     "https://sahealth.sa.gov.au/careers"),

    ("★ Mount Gambier Health SA — 482/186",
     "https://sahealth.sa.gov.au/careers"),

    ("★ Port Pirie Regional Health SA — 482",
     "https://sahealth.sa.gov.au/careers"),

    ("★ Ceduna District Health SA — 482",
     "https://sahealth.sa.gov.au/careers"),

    ("★ Coober Pedy Hospital SA — 482",
     "https://sahealth.sa.gov.au/careers"),

    ("★ SA Health — All Nursing Jobs",
     "https://sahealth.sa.gov.au/careers"),

    # ── AU NATIONAL AGED CARE — 482/186 SPONSORS ─────────

    ("★ Bupa Aged Care Australia — 482/186",
     "https://careers.bupa.com.au/"),

    ("★ Opal HealthCare — 482/186",
     "https://www.opalhealthcare.com.au/careers/"),

    ("★ Estia Health — 482/186 (Overseas page!)",
     "https://www.estiahealth.com.au/careers/application-process/overseas-applications/"),

    ("★ Regis Aged Care — 482/186",
     "https://www.regis.com.au/careers/"),

    ("★ Allity Aged Care — 482/186",
     "https://www.allity.com.au/careers/"),

    ("★ Calvary Health Care — 482/186",
     "https://www.calvarycare.org.au/careers/"),

    ("★ St Vincents Care — 482/186",
     "https://www.svha.org.au/about-svha/careers"),

    ("★ Mercy Health National — 482/186",
     "https://www.mercy.com.au/careers"),

    ("★ RSL LifeCare NSW/ACT — 482/186",
     "https://www.rsllifecare.org.au/careers/"),

    ("★ Bolton Clarke QLD — 482/186",
     "https://www.boltonclarke.com.au/careers/"),

    ("★ Blue Care QLD — 482/186",
     "https://www.bluecare.org.au/careers/"),

    ("★ Ozcare QLD — 482/186",
     "https://www.ozcare.org.au/careers/"),

    ("★ Churches of Christ QLD — 482/186",
     "https://www.cofc.com.au/careers/"),

    ("★ Benetas VIC — 482/186",
     "https://www.benetas.com.au/careers/"),

    ("★ Uniting AgeWell VIC — 482/186",
     "https://www.unitingagewell.org/careers/"),

    ("★ Lyndoch Living VIC — 482/186",
     "https://www.lyndoch.com.au/careers/"),

    ("★ Resthaven Inc SA — 482/186",
     "https://www.resthaven.asn.au/careers/"),

    ("★ Helping Hand SA — 482/186",
     "https://www.helpinghand.org.au/careers/"),

    ("★ Eldercare SA — 482/186",
     "https://www.eldercare.net.au/careers/"),

    ("★ Southern Cross Care SA — 482/186",
     "https://www.southerncrosscare.com.au/careers/"),

    ("★ Respect Aged Care VIC/TAS/SA — 482/186",
     "https://careers.respect.com.au/"),

    ("★ Japara Healthcare VIC/QLD — 482/186",
     "https://www.japara.com.au/careers/"),

    ("★ HammondCare NSW/VIC/QLD — 482/186",
     "https://www.hammond.com.au/careers/"),

    ("★ Arcare VIC/QLD/NSW — 482/186",
     "https://www.arcare.com.au/careers/"),

    ("★ Catholic Healthcare NSW — 482/186",
     "https://www.catholichealthcare.com.au/careers/"),

    ("★ BaptistCare NSW/WA — 482/186",
     "https://www.baptistcare.org.au/careers/"),

    ("★ Anglicare NSW — 482",
     "https://www.anglicare.org.au/careers/"),

    ("★ McLean Care NSW/QLD — 482",
     "https://www.mcleancare.org.au/careers/"),

    # ── AU DISABILITY / NDIS ──────────────────────────────

    ("★ Life Without Barriers AU — 482",
     "https://www.lwb.org.au/careers/"),

    ("★ Scope Australia — 482",
     "https://www.scopeaust.org.au/careers/"),

    ("★ Endeavour Foundation QLD — 482",
     "https://www.endeavour.com.au/careers/"),

    ("★ Just Better Care AU — 482",
     "https://www.justbettercare.com/careers/"),

    ("★ Right at Home Australia — 482",
     "https://www.rightathome.com.au/careers/"),

    ("★ Home Instead Senior Care — 482",
     "https://www.homeinstead.com.au/careers/"),

    ("★ Prestige Inhome Care VIC — 482",
     "https://www.prestigeinhomecare.com.au/careers/"),

    # ── AU HOSPITAL NETWORKS ──────────────────────────────

    ("★ Ramsay Health Care — 482/186",
     "https://careers.ramsayhealth.com.au/"),

    ("★ St John of God Health Care — 482/186",
     "https://www.sjog.org.au/careers/"),

    ("★ Epworth HealthCare VIC — 482/186",
     "https://www.epworth.org.au/careers/"),

    ("★ Austin Health Melbourne — 482/186",
     "https://www.austin.org.au/careers/"),

    ("★ Werribee Mercy Hospital VIC — 482/186",
     "https://www.mercy.com.au/careers"),

    # ── AU RECRUITMENT AGENCIES ───────────────────────────

    ("★ Medacs Healthcare AU — Best Agency",
     "https://apac.medacs.com/find-a-job/"),

    ("★ Healthcare Australia Agency",
     "https://healthcareaustralia.com.au/find-a-job/"),

    ("★ Cornerstone Medical AU",
     "https://www.cornerstonemedical.com.au/jobs/"),

    ("★ Hays Healthcare AU",
     "https://www.hays.com.au/healthcare-medical"),

    ("★ Randstad Healthcare AU",
     "https://www.randstad.com.au/healthcare/"),

    ("★ JPS Medical Recruitment AU",
     "https://www.jpsmedical.com/au/jobs/"),

]

# ══════════════════════════════════════════════════════════
# SECTION 3 — JOB BOARD SEARCHES (Real-time jobs!)
# ══════════════════════════════════════════════════════════

JOB_BOARDS = [

    # NZ Job Boards
    ("🇳🇿 SEEK NZ — HCA Visa Sponsorship",
     "https://www.seek.co.nz/jobs?keywords=health+care+assistant+visa+sponsorship&daterange=3"),

    ("🇳🇿 SEEK NZ — RN AEWV Green List",
     "https://www.seek.co.nz/jobs?keywords=registered+nurse+AEWV&daterange=3"),

    ("🇳🇿 SEEK NZ — Aged Care Nurse Sponsor",
     "https://www.seek.co.nz/jobs?keywords=aged+care+nurse+sponsorship&daterange=3"),

    ("🇳🇿 SEEK NZ — AIN Assistant Nursing",
     "https://www.seek.co.nz/jobs?keywords=assistant+in+nursing&daterange=3"),

    ("🇳🇿 Indeed NZ — HCA Sponsorship",
     "https://nz.indeed.com/jobs?q=health+care+assistant+visa+sponsorship&fromage=3"),

    ("🇳🇿 Indeed NZ — RN AEWV",
     "https://nz.indeed.com/jobs?q=registered+nurse+AEWV+sponsorship&fromage=3"),

    ("🇳🇿 TradeMe Jobs — HCA Visa NZ",
     "https://www.trademe.co.nz/a/jobs/search?search_string=health+care+assistant+visa"),

    ("🇳🇿 Jooble NZ — HCA Sponsorship",
     "https://nz.jooble.org/jobs-health-care-assistant-visa-sponsorship/New-Zealand"),

    ("🇳🇿 Jora NZ — RN Visa",
     "https://nz.jora.com/Registered-Nurse-With-Visa-Sponsorship-jobs"),

    # AU Job Boards
    ("🇦🇺 SEEK AU — RN 482 Sponsorship",
     "https://www.seek.com.au/jobs?keywords=registered+nurse+482+sponsorship&daterange=3"),

    ("🇦🇺 SEEK AU — HCA 482 Visa",
     "https://www.seek.com.au/jobs?keywords=HCA+482+sponsorship&daterange=3"),

    ("🇦🇺 SEEK AU — Aged Care Nurse Visa",
     "https://www.seek.com.au/jobs?keywords=aged+care+nurse+visa+sponsorship&daterange=3"),

    ("🇦🇺 SEEK AU — AIN 482 Regional",
     "https://www.seek.com.au/jobs?keywords=AIN+482+regional+sponsorship&daterange=3"),

    ("🇦🇺 SEEK AU — Personal Care Worker Visa",
     "https://www.seek.com.au/jobs?keywords=personal+care+worker+visa+sponsorship&daterange=3"),

    ("🇦🇺 Indeed AU — Aged Care 482",
     "https://au.indeed.com/jobs?q=aged+care+482+visa+sponsorship&fromage=3"),

    ("🇦🇺 Indeed AU — RN 482 Sponsorship",
     "https://au.indeed.com/jobs?q=registered+nurse+482+sponsorship&fromage=3"),

    ("🇦🇺 Jooble AU — Aged Care Visa",
     "https://au.jooble.org/jobs-aged-care-visa-sponsorship/Australia"),

    ("🇦🇺 HealthcareLink AU",
     "https://www.healthcarelink.com.au/jobs/search?q=registered+nurse+sponsorship"),

    ("🇦🇺 Nursing Jobs AU",
     "https://www.nursingjobs.com.au/jobs?q=registered+nurse+sponsorship"),

    # India Job Boards
    ("🇮🇳 Naukri — Nurse New Zealand",
     "https://www.naukri.com/nurse-jobs-in-new-zealand"),

    ("🇮🇳 Naukri — Nurse Australia",
     "https://www.naukri.com/nurse-jobs-in-australia"),

    ("🇮🇳 Indeed India — RN NZ Sponsorship",
     "https://in.indeed.com/jobs?q=registered+nurse+New+Zealand+sponsorship&fromage=7"),

    ("🇮🇳 Indeed India — RN AU Sponsorship",
     "https://in.indeed.com/jobs?q=registered+nurse+Australia+sponsorship&fromage=7"),

    ("🇮🇳 Shine — Nurse Abroad",
     "https://www.shine.com/job-search/nurse-jobs-abroad/"),

    # LinkedIn
    ("🌍 LinkedIn — RN NZ Sponsorship",
     "https://www.linkedin.com/jobs/search/?keywords=registered+nurse+visa+sponsorship+New+Zealand&f_TPR=r259200"),

    ("🌍 LinkedIn — HCA Australia 482",
     "https://www.linkedin.com/jobs/search/?keywords=HCA+482+visa+sponsorship+Australia&f_TPR=r259200"),

    ("🌍 LinkedIn — Aged Care Nurse NZ AU",
     "https://www.linkedin.com/jobs/search/?keywords=aged+care+nurse+sponsorship+Australia+New+Zealand&f_TPR=r259200"),

]

# ══════════════════════════════════════════════════════════
# WRITE COMPLETE FILE
# ══════════════════════════════════════════════════════════

results.append(f"SECTION 1 — NZ HOSPITALS ({len(NZ_HOSPITALS)} DIRECT CAREER LINKS)\n")
results.append("Apply directly on their websites — no middleman!\n")
results.append("="*60 + "\n\n")
for name, url in NZ_HOSPITALS:
    results.append(f"{name}\n→ APPLY: {url}\n\n")

results.append(f"\nSECTION 2 — AUSTRALIA HOSPITALS ({len(AU_HOSPITALS)} DIRECT CAREER LINKS)\n")
results.append("★ = Confirmed 482/186 Visa Sponsorship\n")
results.append("="*60 + "\n\n")
for name, url in AU_HOSPITALS:
    results.append(f"{name}\n→ APPLY: {url}\n\n")

results.append(f"\nSECTION 3 — JOB BOARDS ({len(JOB_BOARDS)} LIVE SEARCH LINKS)\n")
results.append("New jobs posted daily — check these every day!\n")
results.append("="*60 + "\n\n")
for name, url in JOB_BOARDS:
    results.append(f"{name}\n→ SEARCH: {url}\n\n")

total = len(NZ_HOSPITALS) + len(AU_HOSPITALS) + len(JOB_BOARDS)
results.append("\n" + "="*60 + "\n")
results.append(f"TOTAL LINKS: {total}\n")
results.append(f"  NZ Hospitals: {len(NZ_HOSPITALS)}\n")
results.append(f"  AU Hospitals: {len(AU_HOSPITALS)}\n")
results.append(f"  Job Boards:   {len(JOB_BOARDS)}\n\n")
results.append(f"YOUR DETAILS:\n")
results.append(f"  Name:  Kartik Melkani\n")
results.append(f"  NCNZ:  APC 367690\n")
results.append(f"  AHPRA: NMW0004061692\n")
results.append(f"  Phone: +91 9410965768\n")
results.append(f"  Email: kartikmelkani123@gmail.com\n\n")
results.append(f"Generated: {datetime.datetime.now()}\n")
results.append(f"JAY SHRI RAM KARTIK! Your job is coming! 🙏\n")

with open("jobs.txt", "w", encoding="utf-8") as f:
    f.writelines(results)

print(f"✅ DONE! {total} sponsorship links saved!")
print(f"  NZ Hospitals: {len(NZ_HOSPITALS)}")
print(f"  AU Hospitals: {len(AU_HOSPITALS)}")
print(f"  Job Boards:   {len(JOB_BOARDS)}")
