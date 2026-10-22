Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Montefiore New Rochelle Hospital: Montefiore New Rochelle Hospital (formerly Sound Shore Medical Center) is a community-based, teaching hospital located at 16 Guion Place in the city of New Rochelle, in Westchester County, New York, and affiliated with the Albert Einstein College of Medicine.  The hospital opened in 1892 as New Rochelle Hospital.  On November 6, 2013, Sound Shore was acquired by the Bronx-based Montefiore Medical Center, the University Hospital for the Albert Einstein College of Medicine, was renamed Montefiore New Rochelle Hospital, and became part of the Montefiore Health System.

WFUV: WFUV, 90.7 FM in New York City, is Fordham University's 47,000-watt effective radiated power noncommercial radio station, with studios on its Bronx campus and its antenna atop nearby Montefiore Medical Center.  First broadcast in 1947, its air staff has included New York City radio veterans Dennis Elsas, Vin Scelsa and Pete Fornatale.  Other full-time air staff members include Rita Houston (program director and host of the program "The Whole Wide World"), Darren DeVivo, Carmel Holt, Corny O'Connell and Alisa Ali.

Montefiore Medical Center: Montefiore Medical Center, in the Norwood section of the Bronx, New York, is a teaching hospital of the Albert Einstein College of Medicine.  It is named for Moses Montefiore and is one of the 50 largest employers in New York State.  In 2016, Montefiore Medical Center was ranked #7 of the 180 New York City metropolitan area hospitals by "U.S. News & World Report".

WCUR: 91.7 WCUR FM "The Curve", also known as West Chester University Radio, is a college radio station that broadcasts in the Philadelphia area via a transmitter that covers a 5-mile radius around West Chester University in West Chester, Pennsylvania.  WCUR offers a wide variety of music, news, sports, and specialty programming.  WCUR is considered a free format station, and it does not require that DJs play within certain parameters.  All undergraduate students of West Chester University are free to participate and become DJs.  WCUR began as WCSC AM 64, a carrier current station only available on campus.  The call sign WCUR was being used in 1974.  In 1976 the on air slogan became 64CUR and a Part 15 FM transmission was added at .1 watt to serve the Sykes Student Union building and extend across the street to Killnger Hall.  Efforts began at that time to seek a class A FM license, but funds were not approved.  In the mid-1980s the station changed its call letters to WCUR AM 68, but it remained a carrier current station.  In 1998, the station received a construction permit to build an FM station, and after installing a broadcast transmitter and antenna atop Sykes Student Union in the summer of 1999, the station signed on as WCUR 91.7 FM on September 1, 1999.  Since 2001, WCUR also streams live on air from anywhere in the world from its website, www.wcur.org.

WNBM: WNBM (103.9 FM) is a radio station licensed to Bronxville, New York, United States, a suburban village north of New York City.  Branded on-air as Radio 103.9, the station features an urban adult contemporary format and is owned by Atlanta-based Cumulus Media.  WNBM shares studios with sister stations WABC (770 AM), WNSH (94.7 FM) and WPLJ (95.5 FM) above Pennsylvania Station in Midtown Manhattan, and its transmitter is based on the campus of Montefiore Medical Center in the Bronx, New York City's northernmost borough.

Fordham University: Fordham University ( ) is a private, independent research university in New York City, founded by the Catholic Diocese of New York in 1841.  It is the oldest Catholic institution of higher education in the northeastern United States, and the third-oldest university in New York.

WFUV: City Folk Live VII: WFUV: City Folk Live VII is a compilation album released by WFUV (90.7 FM in New York City) in November 2004 to highlight songs performed live in the studio by some of the year's favorite guests.  Money raised from the album supported WFUV, Fordham University's non-commercial radio station, with studios on campus and its 50,000-watt transmitter atop nearby Montefiore Medical Center.

Steven Libutti: Steven K. Libutti, M.D., F.A.C.S. (born April 18, 1964) is an American surgeon and scientist.  In January 2017, he became the third permanent Director of the Rutgers Cancer Institute of New Jersey, Vice Chancellor for Cancer Programs for Rutgers Biomedical Health Sciences and the Senior Vice President for Oncology Services for RWJBarnabas Health, the largest health system in New Jersey.  He is a tenured Professor of Surgery at the Rutgers Robert Wood Johnson Medical School.  Libutti's work on the study of tumor angiogenesis and the tumor microenvironment has led to novel approaches for the treatment of cancer.  He is also one of the pioneers of regional and targeted cancer therapy.  He was the founding Director of the Montefiore-Einstein Center for Cancer Care, and served as the Associate Director of the Albert Einstein Cancer Center and Vice-Chairman of the Department of Surgery at Montefiore Medical Center and the Albert Einstein College of Medicine from 2009-2017.  Libutti was a tenured Professor of Surgery and Genetics at the Albert Einstein College of Medicine in the Bronx, New York and a Professor of Surgery at the Uniformed Services University of the Health Sciences in Bethesda, Maryland.  In September, 2009, Libutti was invested as "The Marvin L. Gliedman, M.D. Distinguished Surgeon" in the Department of Surgery at Montefiore Medical Center.  Libutti is the Editor-in-Chief of the Springer Nature journal, Cancer Gene Therapy.

WSYY-FM: WSYY-FM (94.9 FM) is a radio station broadcasting for approximately 18¼ hours per day, 7 days a week (from 4:55AM through 11:10PM ET) under the slogan, ""Radio With An Attitude"".  Playing a mix of oldies/classic hits, adult contemporary, rock music, and some country crossovers, the station broadcasts an Adult Hits/Full-Service format for approximately 16 hours per day, from 6:00AM through 10:00PM ET (reserving the first and, also, the final hour of their broadcast day to "When Radio Was").  "The Mountain 94.9" carries local high school sports in season.  "The Mountain 94.9" had also carried the complete schedule of Red Sox Baseball (from 1997 through 2015, prior to becoming a Former Affiliate in 2016, which was when Millinocket's affiliation with the Red Sox Baseball would ultimately be transferred over to co-owned WSYY-AM, thus concluding the frequent interruptions to the music on "The Mountain 94.9" during Baseball season).  The station currently features programming from CBS Radio and carries CBS Radio News at the top of every hour (and has been an affiliate of that network for many decades).  Licensed to Millinocket, Maine, United States, the station's broadcast signal serves the Central Penobscot County, Eastern Piscataquis County, and Southern Aroostook County Maine areas, and the station is licensed to serve the town of Millinocket, Maine, the very town where its studios/offices and tower site are located.  The station is currently owned by Katahdin Communications, Inc.  WSYY-FM originally went on the air in 1978 on 97.7 FM as WKTR, upgrading to its current facilities in 1984 on 94.9.  Prior to their "The Mountain 94.9" branding, WSYY-FM used to be referred to as "North Country 95", airing a full-time Country Music format.  The current format, branding, and slogan was probably adopted around March 1, 2004, when Katahdin Communications, Inc. assumed control of WSYY-FM & WSYY-AM from Katahdin Timberlands, LLC (as a result of the radio station facing increasing land disputes), initially as a short term lease agreement but the transfer of ownership ultimately became permanent.  Those same land disputes would eventually lead to a loss of WSYY-FM's 23,500 watt transmitter location (featuring an antenna HAAT of 211 meters); as a result, WSYY-FM may have been operating under a Special Temporary Authority License (a 12,000 watt facility with an antenna HAAT of 68 meters via Hammond Ridge on Lake Road, about two miles from Millinocket Municipal Airport), ever since as long ago as late 2007, pending a planned permanent move to a 22,000 watt facility with an antenna HAAT of 198.4 meters (from just off Nicatou Road in Medway, well east of WSYY-FM's old or current transmitter tower location).  On November 23th, 2016, the CP for this proposed move was modified to a 45,000 watt facility with an antenna HAAT of 146.7 meters, the first time this proposed move has ever received official approval from the FCC.  WSYY-FM is one of the two Maine affiliates—apart from WLOB—of When Radio Was (7 days a week from 5:00AM through 6:00AM ET and also from 10:00PM through 11:00PM ET), is one of the two Maine affiliates (WWMJ) of The Acoustic Storm (Saturdays from 9:00AM through 12:00PM ET), is Maine's only affiliate of the Crook & Chase syndicated Country Music countdown programming (Sunday afternoons from 2:00PM through 6:00PM ET), and is an affiliate of the Blues Deluxe radio show.  WSYY-FM/WSYY-AM are unusual in that while these stations are authorized to broadcast 24 hours a day, the stations both have sign-offs every day (WSYY-AM signing off at sun-down, broadcasting only on Weekends (but not between Monday-through-Friday) and WSYY-FM broadcasting for approximately 18¼ hours per day, 7 days a week, WSYY-FM's broadcast day concluding with the 11:00PM ET Top-of-the-Hour CBS Radio newscast and then a Nightly Sign-Off Announcement and then an instrumentation of the American national anthem, followed by Dead Air amidst a Transmitter Power-Down, not Signing Back Onto The Air until 4:55AM ET).  In Old Town and also Bangor (and continuing southward and/or southwestward), the station has strong FM co-channel interference with Portland-market WHOM (which transmits from atop Mount Washington in New Hampshire, the tallest peak in the Northeast and had for a long time claimed on its website that it has the largest coverage area of any FM station in the United States, its signal spanning five states: NH, ME, VT, MA, NY and also parts of Southern Quebec Province, Canada), this matter being especially problematic before dawn or after dusk.  In favorable atmospheric conditions, a very weak signal of WHOM can be DX-ed in Millinocket during overnight hours (when WSYY-FM is off-the-air).

Robert E. Michler: Robert E. Michler, MD is an American surgeon who specializes in complex heart surgery, especially mitral and aortic valve repair.  He is Surgeon-in-Chief at Montefiore Medical Center and Albert Einstein College of Medicine in New York, New York.  He is also the Samuel I. Belkin Chair, Professor and Chairman, Department of Cardiovascular and Thoracic Surgery, Professor and Chairman, Department of Surgery and Co-Director, Montefiore Einstein Center for Heart and Vascular Care.

Question: What old, Catholic university is home to a radio station with its antenna atop the Montefiore Medical Center?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The name of the university."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the university was founded."
    },
    "is_catholic_institution": {
      "type": "boolean",
      "description": "Indicates if the university is a Catholic institution."
    },
    "associated_radio_station": {
      "type": "object",
      "properties": {
        "station_call_sign": {
          "type": "string",
          "description": "The call sign of the radio station."
        },
        "frequency_fm": {
          "type": "string",
          "description": "The FM frequency of the radio station."
        },
        "antenna_location_description": {
          "type": "string",
          "description": "A description of the radio station's antenna location."
        }
      },
      "required": [
        "station_call_sign",
        "frequency_fm",
        "antenna_location_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "university_name",
    "founding_year",
    "is_catholic_institution",
    "associated_radio_station"
  ],
  "additionalProperties": false
}
