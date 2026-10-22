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
Robert Ward Johnson: Robert Ward Johnson (July 22, 1814 – July 26, 1879) was an American politician who served as a Confederate States Senator from Arkansas (1862-1865).  He previously served as a U.S. Representative (1847-1853), Senator (1853-1861), and delegate to the Provisional Congress of the Confederate States (1861-1862).

William S. Barry: William S. Barry (born William Taylor Sullivan Barry; December 10, 1821 – January 29, 1868) was an American politician who served as member of the Provisional Congress of the Confederate States from Mississippi.  Prior to this Barry served as a member of the U.S. House of Representatives from Mississippi's 2nd congressional district.

Mississippi's 2nd congressional district: Mississippi's 2nd congressional district (MS-2) is the only majority-black district in the state, covering much of western Mississippi.  The district includes most of Jackson, the riverfront cities of Greenville and Vicksburg, and the interior market cities of Clarksdale, Greenwood, and Clinton.  The district is approximately 275 mi long, 180 mi wide and borders the Mississippi River; it encompasses much of the Mississippi Delta, and a total of 15 counties and parts of several others.

Francis S. Bartow: Francis S. Bartow (born Francis Stebbins Bartow; September 6, 1816 – July 21, 1861) was a licensed attorney turned politician, serving two terms in the United States House of Representatives and becoming a political leader of the Confederate States of America.  Bartow was also a colonel in the Georgia Militia commanding the 21st Oglethorpe Light Infantry during the early months of the American Civil War.  Bartow was a delegate from Georgia's 1st congressional district to the Southern Convention in Montgomery, Alabama becoming an inaugurating member of the Confederate Provisional Congress—leading efforts to prepare defensive forces for an impending federal invasion which did occur, protracting into The American Civil War of 1861–65.

Francis Burton Craige: Francis Burton Craige (March 13, 1811 – December 30, 1875) was a Congressional Representative from North Carolina; born near Salisbury, North Carolina, March 13, 1811; attended a private school in Salisbury, and was graduated from the University of North Carolina at Chapel Hill in 1829; editor and proprietor of the Western Carolinian 1829–1831; studied law; was admitted to the bar in 1832 and commenced practice in Salisbury; one of the last borough representatives in the State house of representatives 1832–1834; elected as a Democrat to the Thirty-third and to the three succeeding Congresses (March 4, 1853 – March 3, 1861); chairman, Committee on Public Buildings and Grounds (Thirty-third Congress); delegate to the State secession convention in 1861 and introduced the Ordinance of Secession in the form in which it was adopted; delegate to the Provisional Congress of the Confederate States which met in Richmond, Virginia, in July 1861; died in Concord, North Carolina, while attending the courts of that county, December 30, 1875; interment in Old English Cemetery, Salisbury, North Carolina.

Albert Rust: Albert Rust (c. 1818 – April 4, 1870) was an American politician who served as a delegate from Arkansas to the Provisional Congress of the Confederate States from 1861 to 1862.  A member of the Democratic Party, Rust was the U.S. Representative from Arkansas 's 2 congressional district , serving from 1859 to 1861.  Rust also served as a senior officer of the Confederate States Army during the American Civil War.

Confederate States Army: The Confederate States Army (C.S.A.) was the military ground force of the Confederate States of America (Confederacy) during the American Civil War (1861-1865).  On February 28, 1861, the Provisional Confederate Congress established a provisional volunteer army and gave control over military operations and authority for mustering state forces and volunteers to the newly chosen Confederate president, Jefferson Davis (1808-1889), a graduate of the U.S. Military Academy on the Hudson River at West Point, New York, and colonel of a volunteer regiment during the Mexican–American War (1846-1848), later a United States Senator from Mississippi and U.S. Secretary of War in the administration of 14th President Franklin Pierce (1853-1857).  By March 1861, the Provisional Confederate Congress expanded the provisional forces and established a more permanent Confederate States Army.

Provisional Congress of the Confederate States: The Provisional Congress of the Confederate States, also known as the Provisional Congress of the Confederate States of America, was a congress of deputies and delegates called together from the Southern States which became the governing body of the Provisional Government of the Confederate States of America (CSA) from February 4, 1861, to February 17, 1862.  It sat in Montgomery, Alabama, until May 20, 1861, when it adjourned to meet in Richmond, Virginia, on July 20, 1861.  It added new members as other states seceded and directed the election on November 6, 1861, at which a permanent government was elected.

Thomas Hart Ruffin: Thomas Hart Ruffin (September 9, 1820 – October 17, 1863) was a Congressional Representative from North Carolina; born in Louisburg, North Carolina, September 9, 1820; attended the common schools; graduated from the University of North Carolina Law School, Chapel Hill, North Carolina, 1841; lawyer, private practice; circuit attorney of the seventh judicial district of the state of Missouri 1844-1848; elected as a Democrat to the Thirty-third and to the three succeeding Congresses (March 4, 1853 – March 3, 1861); delegate to the Confederate Provisional Congress at Richmond, Va., in July 1861; during the American Civil War served in the Confederate Army as colonel of the First North Carolina Cavalry, Confederate States of America; mortally wounded in action on October 14, 1863, at Auburn, Virginia; died October 17, 1863 in Grace Church Hospital, Alexandria, Virginia; interment in the private cemetery on the Ruffin homestead, near Louisburg, N.C.

Congress of the Confederate States: The Confederate States Congress was both the provisional and "permanent" legislative assembly of the Confederate States of America that existed from 1861 to 1865.  Its actions were for the most part concerned with measures to establish a new national government for the Southern "revolution", and to prosecute a war that had to be sustained throughout the existence of the Confederacy.  At first, it met as a provisional congress both in Montgomery, Alabama and Richmond, Virginia.

Question: Prior to serving as a member of the Provisional Congress of the Confederate States from Mississippi, William S. Barry served as a member of which majority-black district in the state, covering much of western Mississippi?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the politician."
    },
    "prior_role": {
      "type": "string",
      "description": "The political role held by the person prior to the Provisional Congress of the Confederate States."
    },
    "congressional_district": {
      "type": "string",
      "description": "The specific congressional district the person served in."
    },
    "district_attributes": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string",
          "description": "The state to which the congressional district belongs."
        },
        "is_majority_black": {
          "type": "boolean",
          "description": "Indicates if the district is majority-black."
        },
        "location_description": {
          "type": "string",
          "description": "A description of the geographical area covered by the district."
        }
      },
      "required": [
        "state",
        "is_majority_black",
        "location_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "prior_role",
    "congressional_district",
    "district_attributes"
  ],
  "additionalProperties": false
}
