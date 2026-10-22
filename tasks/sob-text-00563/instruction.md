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
Manalikkara: Manalikkara () is a small village located in the southern part of ancient travancore state, presently under Kanyakumari district of Tamil Nadu in Kalkulam Taluk.  The area comes under Padmanabhapuram division in Kalkulam Taluk in Kothanallur Panchayat.  Presently this place is known as Vazhikkalampadu under revenue department.  The Malayalam name Manalikkara was very popular during the Travancore state rule and after the reformation of Indian states in 1956, this place is more known as Vazhikkalampadu and it became the part of Kanyakumari district of Tamil Nadu.  This area is mostly covered with Malayalam speaking families.  The core places in Manalikkara are Azhuvar Sree Krishna Swamy Temple and Ancient Manalikkara Madom.  Sree Kailasam temple, Muttakadu and 6th Sivalaya temple Pannipaham temple are a kilometer away from this place.  The world heritage centre and the first capital city of travancore, Padmanabhapuram and the Padmanabhapuram palace is located a few kilometers away from Manalikkara.

Naval Submarine Base New London: Naval Submarine Base New London is the United States Navy's primary East Coast submarine base, also known as the "Home of the Submarine Force".  It is located in Groton, Connecticut.

Masonville Place: Masonville Place (known locally as Masonville or Masonville Mall, and corporately styled as "CF Masonville Place") is a two-storey regional shopping mall located in London, Ontario, Canada, at the southeast corner of Fanshawe Park Road and Richmond Street.  The mall contains over 130 stores, several restaurants, and a food court.  Masonville Place is anchored by several large retailers including Hudson's Bay, Forever 21, Zara, H&M, Sport Chek/Atmosphere, and Shoppers Drug Mart.  The SilverCity Cinemas are also located at the shopping centre, featuring a small arcade and an IMAX theatre.  It is owned by Cadillac Fairview Corporation Limited.

Poojappura: Poojappura known as "The heart of Trivandrum" is a place in the city of Thiruvananthapuram (Trivandrum) in India.  This place located in the south-east part of the city, surrounded by Jagathi, Karamana, Mudavanmugal and Thirumala in its 4 sides.  This place was once used as the worship place during the Navaratri festival season.  The name Poojappura comes from the fact that it was here that the King of Travancore used to arrive during Mahanavami celebrations for the "pooja"(worship). There is biggest Kavadi Procession on Vijayadeshami day with over 700 Kavadis,Paravakavadi,Suryakavadi,Mayilkavadi,Agnikavadi etc.

Shukachari: Shukachari is a hill place located in the hill ranges known as Mahadev Hills between Atpadi and Khanapur of Sangli district, Maharashtra, India.  As per "Puran" this place is believed to be the place of the epic sage Shukamuni or Shuka, son of Vyas.  This is a very popular place in Atpadi taluka, people come from all the places of taluka as well as from outside.  This is famous for Big Stones & Dark Forest as well as a water source in between mountains.

Naval Submarine Medical Research Laboratory: The Naval Submarine Medical Research Laboratory (NSMRL) is located on the New London Submarine Base in Groton, Connecticut.  The laboratory's mission is to protect the health and enhance the performance of United States War Fighters through focused submarine, diving, and surface research solutions.  It is a subordinate command of the Naval Medical Research Center.

Harrington Place, Washington: Harrington Place, also known as Herrington Place, is an unincorporated community in Cowlitz County, Washington.  Harrington Place is located east of the city of Castle Rock and along the South Fork Toutle River.  Harrington Place is accessed by about 19 mi of logging roads off of Washington State Route 504, also known as the Spirit Lake Memorial Highway, after reaching the community of Toutle while traveling eastbound.  The Harrington Place community is part of the Kelso School District, a K-12 school district of nearly 5,000 students.

St. Stephen's Basilica, Jerusalem: The St. Stephen's Basilica (Hebrew: מנזר סנט אטיין‎ ‎ ) or simply the Church of St. Stephen, also known by its French name, Saint-Étienne, is the name given to a Catholic church located outside the walls of the Old City of Jerusalem, on the road leading north to Nablus.  It is next to the convent of St. Stephen, home to the French Bible and Archaeology School (École biblique et archéologique française de Jérusalem), and the convent church.  An old tradition sees this place as the place where the martyrdom of Saint Stephen took place, the martyr deacon mentioned in the book of Acts ( ).  A rival site is located in the Kidron Valley.

Shakatapuram: Shakatapuram is a religious place for Hindus located in the Koppa taluk of the state of Karnataka, India.  It is located near Sringeri and is situated on the banks of river Tunga.  It is famous for a Hindu Math called "Shri Vidya Peetam" which is present at this place.  Shakatapuram is also known by the name Bhandigadi.  The Kumbhabhishekam event held at this place attracts a number of devotees.

Kageshwori: Kageshwori (Nepali: कागेश्वरी ) is a religious place in Kageshwori Manahara Municipality-14, (previously Gagalphedi-7) located north-east of Kathmandu, capital city of Nepal.  God Shiva is the attraction of the believers.Etymologically Kageshowri is combination of two words, that is 'Kag' means 'crow' and 'Ishowr' means 'God'.  This means Crow is gloeified here as it has religious and environmental role. " 'Mahadev' is the God of Gods", believers say.  Dudhe Gaun & Puwar Gaun are the nearest villages of this sacred place.  This place is also known as "Kageshwori Temple" or "Kageshwori Mahadevsthan (कागेश्वरी महादेवस्थान)".  One day in Bhadra Sukla Asthami (भाद्र शुक्ल अष्टमी) of each year, thousands of pilgrims come to visit this place.  Golden crow is also shown at that occasion.  Religious importance as well as economic activities are promoted through Haat bazar (Mela). Developing this place as the destination to international pilgrimage spot is on discussion.  It is based on the lap of Shivapuri National Park in the remote bank of Kageshowri (Mahadev) river.

Question: What is the place where NSMRL is located on known as?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "place_name": {
      "type": "string",
      "description": "The primary name of the location where NSMRL is situated."
    },
    "alternative_name": {
      "type": "string",
      "description": "The alternative name or nickname for the location."
    },
    "located_in_city": {
      "type": "string",
      "description": "The city where the location is situated."
    },
    "located_in_state": {
      "type": "string",
      "description": "The state where the location is situated."
    },
    "organization_located": {
      "type": "string",
      "description": "The name of the organization located at this place."
    }
  },
  "required": [
    "place_name",
    "alternative_name",
    "located_in_city",
    "located_in_state",
    "organization_located"
  ],
  "additionalProperties": false
}
