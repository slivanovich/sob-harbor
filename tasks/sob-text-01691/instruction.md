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
MedStar National Rehabilitation Hospital: MedStar National Rehabilitation Network (MedStar NRH) is located in Washington, D.C., and specializes in treating persons with physical disabilities, including spinal cord injury, brain injury, stroke, arthritis, amputation, multiple sclerosis, post-polio syndrome, orthopedic, and other neurological conditions.

Burke Rehabilitation Hospital: Burke Rehabilitation Hospital is a non-profit, 150-bed acute rehabilitation hospital located in White Plains, New York.  It is the only hospital in Westchester County entirely dedicated to rehabilitation medicine.  Opened in 1915, Burke has been involved in medical rehabilitation for over one hundred years.  As of January 2016, Burke is a member of the Montefiore Health System, Inc.

Magee Rehabilitation Hospital: Magee Rehabilitation Hospital, founded in 1958, is a 96-bed specialty medical rehabilitation hospital providing physical and cognitive rehabilitation services.  Magee’s flagship facility is located in Center City Philadelphia.  In addition to the main campus that offers comprehensive services for spinal cord injury, brain injury, stroke, orthopaedic replacement, amputation, pain management and work injury, Magee provides an expanding outpatient network serving the surrounding communities.  In 1985, Magee’s brain injury rehabilitation program became the first in the nation to be accredited by the Commission on the Accreditation of Rehabilitation Facilities.  Magee partnered with Jefferson Hospital to create one of the nation’s 14 federally designated centers for spinal cord injury rehabilitation.  Magee has been rated one of America’s leading rehabilitation hospitals by U.S. News & World Report.  Magee provides treatment to more than 5,000 individuals annually.  Magee is authorized to treat wounded military personnel returning from war.  Magee is not an Obligated Group Affiliate.

Children's National Medical Center: Children’s National Medical Center (formerly DC Children’s Hospital) is ranked among the top 10 children’s hospitals in the country by "U.S. News & World Report."  Located just north of the McMillan Reservoir and Howard University, it shares grounds with Washington Hospital Center, National Rehabilitation Hospital, and the DC Veterans Affairs Medical Center.  Kurt Newman, M.D., has served as the president and chief executive officer of Children’s National since 2011.  Children's National is a not-for-profit institution that performs more than 450,000 visits each year.  Featuring 303 beds and a Level IV NICU, Children's National is the regional referral center for pediatric emergency, trauma, cancer, cardiac and critical care as well as neonatology, orthopaedic surgery, neurology and neurosurgery.

MedStar Washington Hospital Center: MedStar Washington Hospital Center is the largest private hospital in Washington, D.C. A member of MedStar Health, the not-for-profit Hospital Center is licensed for 926 beds.  Health services in primary, secondary and tertiary care are offered to adult and neonatal patients.  It also serves as a teaching hospital for Georgetown University School of Medicine.

Rehabilitation Hospital of Rhode Island: The Rehabilitation Hospital of Rhode Island (also known as Fogarty Hospital) is a private rehabilitation hospital at 116 Eddie Dowling Highway (Route 146A) in the Park Square area of North Smithfield, Rhode Island and with another unit, Landmark Medical Center in Woonsocket, Rhode Island.  The Rehabilitation Hospital "is the only free-standing hospital in Rhode Island devoted exclusively to inpatient and outpatient rehabilitation" and provides treatment for "acute illness, traumatic injury, major surgery or life-altering disease."

MedStar Georgetown University Hospital: MedStar Georgetown University Hospital is one of the national capital area's oldest academic teaching hospitals.  It is a not-for-profit, acute care teaching and research facility located in the Georgetown neighborhood of the Northwest Quadrant of Washington, D.C.  MedStar Georgetown is co-located with the Georgetown University Medical Center and is affiliated with the Georgetown University School of Medicine.  Its clinical services represent one of the largest, most geographically diverse, and fully integrated healthcare and delivery networks in the area.  MedStar Georgetown is home to the internationally known Lombardi Comprehensive Cancer Center, as well as centers of excellence in the neurology, neurosurgery, psychiatry, gastroenterology, transplant and vascular surgery.  Originally named Georgetown University Hospital, it became part of the MedStar Health network in 2000.

National Rehabilitation Hospital (Dublin): The National Rehabilitation Hospital (NRH) in Dun Laoghaire, Dublin, is an Irish publicly funded hospital that provides rehabilitation treatment for patients who have a physical or cognitive disability due to illness or injury.  Although it is funded by the state the hospital is owned by a Catholic religious order, the Sisters of Mercy.

Brad Wenstrup: Brad Robert Wenstrup (born June 17, 1958) is an American politician, Army Reserve officer, and Doctor of Podiatric Medicine, who has been the U.S. Representative for Ohio 's 2 congressional district since 2013.  A Republican, he defeated U.S. Representative Jean Schmidt in the 2012 Republican primary election and Democrat William R. Smith in the 2012 general election.  Wenstrup is a colonel in the U.S. Army Reserve and an Iraq War veteran.  After the shooting of Congressman Steve Scalise on the morning of June 14, 2017, Wenstrup attended to the wounded congressman until he was transported to MedStar Washington Hospital Center.

Jewish Rehabilitation Hospital: The Jewish Rehabilitation Hospital is a bilingual hospital center offering general and specialized services dedicated to rehabilitation.  Located in Laval, Canada, the Jewish Rehabilitation Hospital is the regional center in physical rehabilitation for adult and pediatric clients in the region.

Question: MedStar National Rehabilitation Hospital and MedStar Washington Hospital Center are located in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "hospitals": {
      "type": "array",
      "description": "List of hospitals mentioned in the question and their location status.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the hospital."
          },
          "is_located_in_city": {
            "type": "boolean",
            "description": "True if the hospital is located in the identified common city."
          }
        },
        "required": [
          "name",
          "is_located_in_city"
        ],
        "additionalProperties": false
      }
    },
    "common_location_city": {
      "type": "string",
      "description": "The city where both hospitals are located."
    },
    "number_of_hospitals_found_in_city": {
      "type": "integer",
      "description": "The count of hospitals from the question found in the common city."
    }
  },
  "required": [
    "hospitals",
    "common_location_city",
    "number_of_hospitals_found_in_city"
  ],
  "additionalProperties": false
}
