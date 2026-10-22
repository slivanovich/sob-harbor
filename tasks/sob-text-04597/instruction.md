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
John H. Ebersole: Captain John Henry Ebersole, M.D., MC USN (26 January 1925 – 23 September 1993) a pioneer in submarine medicine and radiation oncology, selected by Admiral Rickover to serve as medical officer aboard the US Navy's first two nuclear powered submarines, the USS "Nautilus" and the USS "Seawolf."  He was the radiologist for NASA that screened the Mercury Seven astronauts for Project Mercury.  Ebersole was the radiologist responsible for the x-rays taken during the autopsy of John F. Kennedy on 22 November 1963 at Bethesda Naval Medical Center.

John Ebersole (educator): John Frederick Ebersole (April 4, 1944 – November 23, 2016) was an American educator, author, columnist, and president of Excelsior College.  He served as president from 2006 to 2016, succeeding C. Wayne Williams, the founding president of the college.

Diener: A diener is a morgue worker responsible for handling, moving, and cleaning the corpse (though, at some institutions dieners perform the entire dissection at autopsy).  Dieners are also referred to as morgue attendants, autopsy technicians, and other titles that can vary from region to region.  The word is derived from the German word Leichendiener, which literally means "corpse servant" (""diener"" means "servant".) .

W. Ironside Bruce: William Ironside Bruce (1876 – 21 March 1921) was a physician in Europe who conducted early research on the use of X-rays.  He headed the X-ray departments at Charing Cross Hospital and at the Hospital for Sick Children.  He wrote an early book on X-ray techniques and he was president of the radiology section of the Royal Society of Medicine.  In 1921, Bruce was diagnosed with aplastic anaemia, which his physicians attributed to his work with X-rays.  He died two months after being diagnosed with the illness.  Bruce's death led to the establishment of an X-ray safety committee in Great Britain.

Luna 21: Luna 21 (Ye-8 series) was an unmanned space mission, and its spacecraft, of the Luna program, also called Lunik 21, in 1973.  The spacecraft landed on the Moon and deployed the second Soviet lunar rover, "Lunokhod 2".  The primary objectives of the mission were to collect images of the lunar surface, examine ambient light levels to determine the feasibility of astronomical observations from the Moon, perform laser ranging experiments from Earth, observe solar X-rays, measure local magnetic fields, and study mechanical properties of the lunar surface material.

John F. Kennedy autopsy: The autopsy of President John F. Kennedy was performed, beginning at about 8 p.m. EST November 22, 1963, on the day of his assassination and ending at about 12:30 AM EST November 23, 1963, at the Bethesda Naval Hospital in Bethesda, Maryland.  The choice of autopsy hospital in the Washington, D.C. area was made by his widow, Jacqueline Kennedy.  She chose the Bethesda Naval Hospital because President Kennedy had been a naval officer.

X-ray motion analysis: X-ray motion analysis is a technique used to track the movement of objects using X-rays.  This is done by placing the subject to be imaged in the center of the X-ray beam and recording the motion using an image intensifier and a high-speed camera, allowing for high quality videos sampled many times per second.  Depending on the settings of the X-rays, this technique can visualize specific structures in an object, such as bones or cartilage.  X-ray motion analysis can be used to perform gait analysis, analyze joint movement, or record the motion of bones obscured by soft tissue.  The ability to measure skeletal motions is a key aspect to one's understanding of vertebrate biomechanics, energetics, and motor control.

Projectional radiography: Projectional radiography is a form of medical imaging that produces two-dimensional images by x-ray radiation.  Radiographic exams are typically performed by radiographers, who are trained, licensed medical professionals.  However, radiographers generally perform other types of medical imaging as well, such as computed tomography, which also uses X-rays but generates axial sections of the body instead of projections.

Washington State Community College: Washington State Community College (WSCC) is a two-year community college located in Marietta, the county seat of Washington County, Ohio.  It was established in 1971 as Washington Technical College.  Thanks to former college president Carson K. Miller, the college moved to its current location in 1991.  Since then it has added the Arts and Sciences Center (1996),the Carson K. Miller Library (1998), the Center for Business and Technology (2003), and the Evergreen Child Development Center (2003).  The college offers over fifty associate degree programs.  The current student enrollment is approximately 2,300 students.  Its current president is Dr. Bradley J. Ebersole.

Limited radiology technician: Limited Radiology Technicians perform X-rays of patients and deliver the images to doctors.  They make no diagnosis but still work closely with patients, explaining procedures, operating the X-ray and other associated equipment.  Technical aspects include positioning patients for X-rays, determining appropriate angle and height of X-ray equipment, and calculating radiation dosages needed to create X-rays of the appropriate density, detail, and contrast, enabling the physician to make an accurate diagnosis.

Question: Where did John Ebersole perform x-rays in the autopsy of a president?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who performed the X-rays."
    },
    "role": {
      "type": "string",
      "description": "The role of the person during the event."
    },
    "event_type": {
      "type": "string",
      "description": "The type of event where X-rays were performed."
    },
    "subject_of_autopsy": {
      "type": "string",
      "description": "The name of the person whose autopsy was performed."
    },
    "location_of_xrays": {
      "type": "string",
      "description": "The specific location where the X-rays were performed."
    },
    "date_of_autopsy": {
      "type": "string",
      "description": "The date when the autopsy took place."
    }
  },
  "required": [
    "person_name",
    "role",
    "event_type",
    "subject_of_autopsy",
    "location_of_xrays",
    "date_of_autopsy"
  ],
  "additionalProperties": false
}
