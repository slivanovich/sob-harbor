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
Electorate of Baden: The Electorate of Baden was a State of the Holy Roman Empire from 1803 to 1806.  In 1803, Napoleon bestowed the office of Prince-elector to Charles Frederick.  This only lasted until 1806, when Francis II dissolved the Empire.  When the Holy Roman Empire dissolved, Baden achieved sovereignty, and Charles Frederick became Grand Duke.

Matthew Buchanan: Matthew Buchanan is a fictional character on the American soap opera "One Life to Live".  Born onscreen in 1999, the character was rapidly aged in 2001 with the casting of Eddie Alderson, re-establishing his birth year as 1994 (which is also Alderson's birth year).  Alderson stayed with the series until the ABC Daytime finale in 2012.  Upon resuming as a web series via The Online Network, Robert Gorrie was cast in the role and debuted April 29, 2013, ultimately revising his birth year to 1992.

Charles Frederick White (politician, born 1891): Charles Frederick White (23 January 1891 – 27 November 1956) was a Labour Party politician in the United Kingdom.  He was Member of Parliament (MP) for the Western Division of Derbyshire firstly from 1944-1945 as an Independent Labour candidate and subsequently from 1945 to 1950 as the official Labour Party candidate.  He was the son of Charles Frederick White, who had represented the same constituency for the Liberal Party from 1918 to 1923.

Abdur-Razzaq Nurul-Ain: Syed Abdur-Razzaq Nurul-Ain is the successor of the Sufi saint Syed Ashraf Jahangir Semnani.  From amongst the descendants of Syed Abdul Razzaq Jilani, the line of saints of Ashrafia Jilania is one of the most reputed households belonging to the Indo-Pak subcontinent.  Within this line, Syed Abdul Razzaq, popularly known as Nur-ul-Ain, was the heir, disciple and Khalifa of Syed Ashraf Jehangir Semani.  Syed Abdul Razzaq was the son of his maternal cousin.  Syed Abdul Razzaq is the 11th descendant of the greatest Sufi Syed Abdul Qadir Jilani of Jilan, Iraq.  Abdur-Razzaq Nurul-Ain first met Ashraf Jahangir Semnani at the age of twelve years in Baghdad when Ashraf Jahangir Semnani made a visit there and from there on never parted from his company.  He adopted Syed Abdul Razzaq as his son and made him the heir and caretaker.  Originated from the name of Syed Ashraf, this line of saints is still called as Ashrafia.  Syed Ashraf Jehangir Semani died in 808 AH and Syed Abdul Razzaq became the heir to his throne.  After strenuous spiritual training he was bestowed with Khilafat (Spiritual Successor) and from him the Ashrafi spiritual chain flourished.  According to the tradition of Mirat-ul-Asrar, at the time of his death, Syed Ashraf Jehangir Semani was either 106 or 110 years of age.  In Tohfta ul Abrar, his age is written as 120 and year of birth is 688 AH.  Even his adopted son, Syed Abdul Razzaq was 120 of age at the time of his death.  He spent 12 years before he took Bayat and 68 years in travel and in the service of Syed Ashraf Jehangir Semani and the remaining 40 years after the death of his Murshid at the throne of Khilafat.  In accordance to this, his birth year becomes 728, year of arrival in India 740 and year of death 848.  His grave is located next to that of Ashraf Jahangir Semnani in the same Shrine in Kichauccha Sharif, Dist.  Ambedkar Nagar, Uttar Pradesh, India.

Molly Lansing: Molly Lansing is a fictional character of ABC's "General Hospital".  The role has been portrayed by Haley Pullos since 2009.  Molly is the daughter of Ric Lansing and Alexis Davis.  She was born on-screen on November 10, 2005.  In 2009, Molly's birth year is changed to 1998.  In 2012, Molly states that she is 15, effectively making her birth year 1997.

Charles Frederick Menninger: Charles Frederick Menninger (11 July 1862 – 28 November 1953) was a physician who co-founded the Menninger Foundation with his sons, Karl and William.

Charles Close: Colonel Sir Charles Frederick Arden-Close, KBE CB CMG FRS (10 August 1865 – 19 December 1952) was a British geographer and surveyor.  He was Director General of the Ordnance Survey from 1911 to 1922.  His insistence on attention to detail saw the improvement of many attitudes and methods at the Ordnance Survey.  Close's planning saw the production of many maps now viewed as pinnacles in the classic period of map making.  He was born Charles Frederick Close and changed his surname to Arden-Close in 1938 so as to comply with a bequest.

William Grover-Williams: William Charles Frederick Grover-Williams (born William Charles Frederick Grover, 16 January 1903 – February or March 1945), also known as "W Williams", was a Grand Prix motor racing driver and special agent who worked for the Special Operations Executive (SOE) inside France.  He organised and coordinated the "Chestnut" network.  He was captured and executed by the Nazis.

Karl Menninger: Karl Augustus Menninger (July 22, 1893 – July 18, 1990) was an American psychiatrist and a member of the Menninger family of psychiatrists who founded the Menninger Foundation and the Menninger Clinic in Topeka, Kansas.

Baron Donington: Baron Donington, of Donington Park in the County of Leicester, was a title in the Peerage of the United Kingdom.  It was created in 1880 for Charles Frederick Abney-Hastings.  Born Charles Frederick Clifton, he was the widower of Edith Mary Abney-Hastings, 10th Countess of Loudoun.  He and his wife had in 1859 assumed by Royal licence the surname of Abney-Hastings on succeeding to the Abney-Hastings estates after the death of his wife's kinsman Sir Charles Abney-Hastings, 2nd Baronet in 1858 (see Abney-Hastings baronets).  They were both succeeded by their eldest son Charles Edward Rawdon-Hastings, 11th Earl of Loudoun and 2nd Baron Donington.  However, on his death in 1920 the titles separated.  The Scottish earldom was inherited by his niece Edith, daughter of his second brother the Hon. Major Paulyn Francis Cuthbert Rawdon-Hastings.  The barony of Donington, which could only be inherited by male heirs, passed to his third brother Gilbert Theophilus, who became the third Baron.  He had four daughters but no sons, and on his death in 1927 the barony became extinct.

Question: What was the birth year of the son of Charles Frederick Menninger who died in 1990?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the son of Charles Frederick Menninger who died in 1990."
    },
    "relationship_to_father": {
      "type": "string",
      "description": "The relationship of the identified person to Charles Frederick Menninger."
    },
    "father_name": {
      "type": "string",
      "description": "The name of the father."
    },
    "death_year": {
      "type": "integer",
      "description": "The year the identified person died."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the identified person."
    }
  },
  "required": [
    "person_name",
    "relationship_to_father",
    "father_name",
    "death_year",
    "birth_year"
  ],
  "additionalProperties": false
}
