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
Carlos Montezuma: Carlos Montezuma or Wassaja (born c.1866; died 1923) was a Yavapai-Apache Native American,activist and a founding member of the Society of American Indians.  His birth name Wassaja, means "Signaling" or "Beckoning" in his native tongue.  Wassaja was kidnapped by Pima raiders along with other children to be sold or bartered.  Wassaja was then purchased by an Italian photographer Carlo Gentile in Adamsville, for thirty silver dollars.  Gentile renamed him "Carlos Montezuma".  Montezuma was the first Native American student at the University of Illinois and Northwestern University, and only the second Native American ever to earn a medical degree in an American University after Susan La Flesche Picotte.  Wassaja was the first Native American male to receive a medical degree.  Until his death Wassaja fought to support the rights of his Yavapai people and other Native Americans.

Stanley C. Cox: Stanley Cullen Cox (July 2, 1883 - June 7, 1942) was an American physician who was the head of the Medical Division of the Office of Civilian Defense at the time of his death in 1942.  He was born in 1884 in South Hadley, Massachusetts.  He attended Holyoke High School and Williston Academy before enrolling at the University of Michigan.  He received a bachelor's degree from Michigan in 1908 and a medical degree in 1910.  While attending Michigan, he played on the school's first basketball team, the 1908–09 Michigan Wolverines men's basketball team.  After receiving his medical degree from Michigan, Cox was employed at Gouverneur Hospital in New York for two years.  He then returned to Holyoke, Massachusetts, where he went into private practice.  He served as a military surgeon during World War I and became the head of the Medical Division of the Office of Civilian Defense during World War II.  He was married to Almira Fay Leavitt in June 1912.  They had three daughters and two sons.  He died at age 58 in June 1942 from a heart attack while marching in an "On To Victory" parade in Holyoke.

Emily Blackwell: Emily Blackwell (October 8, 1826 – September 7, 1910) was the second woman to earn a medical degree at what is now Case Western Reserve University, and the third woman (after Elizabeth Blackwell and Lydia Folger Fowler) to earn a medical degree in the United States.

Ernie Fletcher: Ernest Lee "Ernie" Fletcher (born November 12, 1952) is an American physician and politician.  In 1998, he was elected to the first of three consecutive terms in the United States House of Representatives; he resigned in 2003 after being elected the 60th governor of Kentucky and served until 2007.  Prior to his entry into politics, Fletcher was a family practice physician and a Baptist lay minister.  He is the second physician to be elected Governor of Kentucky; the first was Luke P. Blackburn in 1879.  He is a member of the Republican Party.

Joseph Clay Stiles Blackburn: Joseph Clay Stiles Blackburn (October 1, 1838September 12, 1918) was a Democratic Representative and Senator from Kentucky.  He was the younger brother of Kentucky governor Luke P. Blackburn.  Blackburn, a skilled and spirited orator, was also a prominent trial lawyer known for his skill at swaying juries.

Direct bs/md: Direct BS/MD Programs, also known as Combined BS/MD programs or Dual degree program, offered by specific universities and colleges across the America that awards a Bachelor's Degree in Science (B.S.) and a Medical Degree (M.D.).  Depending on the program, the student may earn a Bachelor's Degree in Arts (B.A.).  These programs are highly competitive and are directed toward high school students who are interested in medicine.  Some universities like Texila American University waive the MCAT exam for admission into the program's affiliated medical school while other program require a certain score on the MCAT.  There are over 70 programs in the country that offer this type of admission for high school students.

Kazue Togasaki: Kazue Togasaki (June 29, 1897 – December 15, 1992) was one of the first two women with Japanese ancestry to earn a medical degree in the United States.  The other such woman was Megumi Shinoda, and they both earned their medical degrees in 1933.  Togasaki earned her medical degree from the Woman's Medical College of Pennsylvania in 1933.

Transylvania University: Transylvania University is a private university in Lexington, Kentucky, United States.  It was founded in 1780, making it the first university in Kentucky and among the oldest in the United States.  It offers 36 major programs, as well as dual-degree engineering programs, and is accredited by the Southern Association of Colleges and Schools.  Transylvania's name, meaning "across the woods" in Latin, stems from the university's founding in the heavily forested region of western Virginia known as the Transylvania Colony, which became most of Kentucky in 1792.  Transylvania is the alma mater of two U.S. vice presidents, two U.S. Supreme Court justices, fifty U.S. senators, 101 U.S. representatives, 36 U.S. governors, and 34 U.S. ambassadors, making it a large producer of U.S. statesmen.  Its medical program graduated 8,000 physicians by 1859.  Its enduring footprint, both in national and Southern academia, make it among the most prolific cultural establishments and the most storied institutions in the South.

Luke P. Blackburn: Luke Pryor Blackburn (June 16, 1816September 14, 1887) was an American physician, philanthropist, and politician from Kentucky.  He was elected the 28th governor of Kentucky, serving from 1879 to 1883.  Until the election of Ernie Fletcher in 2003, Blackburn was the only physician to serve as governor of Kentucky.  After earning a medical degree at Transylvania University, Blackburn moved to Natchez, Mississippi, and gained national fame for implementing the first successful quarantine against yellow fever in the Mississippi River valley in 1848.  He came to be regarded as an expert on yellow fever and often worked "pro bono" to combat outbreaks.  Among his philanthropic ventures was the construction of a hospital for boatmen working on the Mississippi River using his personal funds.  He later successfully lobbied Congress to construct a series of similar hospitals along the Mississippi.

James E. Cantrill: James Edwards Cantrill (June 20, 1839 – April 5, 1908) was born in Bourbon County, Kentucky.  He served as a Captain in the Confederate States Army Cavalry as a portion of Morgan's Men.  He was elected the 22nd Lieutenant Governor of Kentucky serving from 1879 to 1883 under Governor Luke P. Blackburn.

Question: What Lexington university did Luke P. Blackburn earn a medical degree at?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who earned the degree."
    },
    "degree_type": {
      "type": "string",
      "description": "The type of degree earned."
    },
    "university_name": {
      "type": "string",
      "description": "The name of the university where the degree was earned."
    },
    "university_location": {
      "type": "string",
      "description": "The city where the university is located."
    }
  },
  "required": [
    "person_name",
    "degree_type",
    "university_name",
    "university_location"
  ],
  "additionalProperties": false
}
