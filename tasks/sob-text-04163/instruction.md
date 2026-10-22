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
Sikh Hon Da Maan: Sikh Hon Da Maan is a religious album by Malkit Singh.  The videos were released are, Sikh Hon Da Maan, Chaare Vaar Gaya, Dastaar, Aaja Gur Nanak Aaja Mereh Sahib & Jindeh.

Malkit Singh: Malkit Singh, MBE (Punjabi: ਮਲਕੀਤ ਸਿੰਘ ) (born Malkit Singh Boparai; 13 September 1962) is an England-based Punjabi bhangra singer.  Born in Hussainpur and raised in Nakodar, he moved to Birmingham in 1984.  Singh is the first Punjabi singer to be honoured with an MBE by Queen Elizabeth II at Buckingham Palace.  He is most famous for the songs "Gur Nalo Ishq Mita", "Tootak Tootak Tootiyan", "Kurri Garam Jayee", "Dekh li vilyait", "Chal Hun", and "Jind Mahi", the latter two from the soundtrack to the popular film "Bend It Like Beckham".

Oriental Star Agencies: Oriental Star Agencies is a British based record label, based in the Balsall Heath area of Birmingham.  Some of the artists introduced by the label include Ustad Nusrat Fateh Ali Khan, Malkit Singh, Alam Lohar and Bally Sagoo.

Sinking of Dongfang zhi Xing: MV "Dongfang zhi Xing" (; translated as "Oriental Star" or "Eastern Star") was a river cruise ship that operated in the Three Gorges region of inland China.  On 1 June 2015, the ship was traveling on the Yangtze River in Jianli, Hubei Province with 454 people on board when it capsized in a severe thunderstorm.  On 13 June, 442 deaths were confirmed, with 12 rescued.  It is the deadliest peacetime maritime disaster in China's history, and the worst maritime disaster (including wartime disasters) since the "Taiping" steamer sank in 1949, killing more than 1,500.

DJ Vix: DJ Vix, born and raised in the east of London is a British-Asian DJ/music producer known for his bhangra tracks, as well as his remixes.  In 1996, he formed Dhol n Bass Roadshow that won many awards in coming years.  He has worked in many places across the globe including Vancouver, Rotterdam, Africa, Norway, Melbourne, Sydney, Perth, LA, Chicago, Washington DC, New York, Jumeirah and Delhi (Club Elevate).  Guest mixes and shows on the Asian radio scene have included for the likes of BBC Radio 1, BBC 1xtra and BBC Asian Network.  Signed up in 2002 by the internationally renowned Moviebox label, DJ Vix has received international recognition as a producer of mainstream Asian beats, with a style identical to none (album).  Following on from his debut album DHOL N BASS UNCUT (2002), he produced his next three albums VIX IT UP (2004) and IDENTICAL 2 NONE (2007) and MOVIEBOX VIX TAPE (2008) with 'Ah Chak Bottle Daru Di' featuring Shin from DCS - the longest no.1 track on the BBC Asian Network that held top spot for a record breaking 13 weeks.  In 2009 DJ Vix received his third award, 'Best Club DJ' at the UK Asian Music Awards (UK AMA) held at the Royal Festival Hall.  In 2011, Dj Vix worked in collaboration with Surinder Shinda and Bhinda Jatt (also known as California Bhangra King).  Dj Vix has also worked with artists like Miss Pooja, RnB superstar Jay Sean, Sukbir, Taz Stereo Nation, B21, XLNC, Debi Muksuspuri, H-Dhami and Ajay the ‘Brit Asia Superstar’ winner of 2010.  In 2014, Dj Vix worked in collaboration with Malkit Singh MBE, and produced the track'Desi Beat'.  In 2014, he released another track, 'Marda' feat Hunterz, along with the new album 'MY TURN' from Manjit Pappu.  His next, and fifth solo album titled "Chapter V" is scheduled to be released on 26 February 2015.

Sejong City: Sejong (] ; Hangul: 세종; Hanja: 世宗 ), officially Sejong Special Self-Governing City (Hangul: 세종특별자치시; Hanja: 世宗特別自治市 ) and formerly known as Yeongi (연기, 燕岐 ) County is South Korea's de facto administrative capital city.  In early 2007, the South Korean government created a special administrative district from parts of South Chungcheong Province and North Chungcheong Province provinces, near Daejeon, to relocate nine ministries and four national agencies from Seoul.  The new offices opened on 2 July 2012, with 36 government agencies slated to move there by 2015.

Billo Rani: Billo Rani is a studio album by Malkit Singh released on 20 November 2009.

Malkit Singh Tehang: Malkit Singh Tehang is a long standing leader of the Sikh community in Sandwell.  He is the ex-president of the first and largest Gurdwara (Sikh Temple) in the UK - Guru Nanak Gurdwara Smethwick.

Lee Balterman: Lee Balterman (1920 – March 16, 2012) was an American photographer.  Born in Chicago, Illinois, Balterman graduated from high school in 1938, and later took evening classes in drawing and painting at the Art Institute of Chicago.  In 1942, during World War II, Balterman enlisted in the US Army Reserves.  First stationed in England, he then served in Clichy, France, working as a hospital aide and later as an army photographer.  After being discharged in 1946, Balterman returned to Chicago and began working as a freelance photographer for the Globe, Rapho-Guillumette, and Black Star agencies, as well as producing covers for periodicals such as "Life", "Fortune", and "Sports Illustrated".  He was noted in particular as a photograph of ballet.  He died in 2012, aged 91.

Oriental Mindoro National High School: The Oriental Mindoro National High School (OMNHS) is the flagship campus and the largest public high school in Oriental Mindoro.  It was established in 1921 and is located in San Vicente East, Calapan City.  It offers high school education from first year to fourth year.  The school is headed by Dr. Nimrod Bantigue.  It was formerly named Oriental Mindoro High School and Jose J. Leido, Jr.  Memorial National High School.

Question: In what year did Malkit Singh move to the city where Oriental Star Agencies is based?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "record_label_name": {
      "type": "string",
      "description": "The name of the record label."
    },
    "city_of_relocation": {
      "type": "string",
      "description": "The city to which the artist moved."
    },
    "year_of_relocation": {
      "type": "integer",
      "description": "The year the artist moved to the specified city."
    },
    "label_location_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the record label is based."
        },
        "area": {
          "type": "string",
          "description": "The specific area within the city where the record label is based."
        }
      },
      "required": [
        "city"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "record_label_name",
    "city_of_relocation",
    "year_of_relocation",
    "label_location_details"
  ],
  "additionalProperties": false
}
