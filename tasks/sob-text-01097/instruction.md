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
Dawes Rolls: The Dawes Rolls (or Final Rolls of Citizens and Freedmen of the Five Civilized Tribes, or Dawes Commission of Final Rolls) were created by the United States Dawes Commission.  The Commission, authorized by United States Congress in 1893, forced the Five Civilized Tribes to agree to a land allotment plan and dissolution of the reservation system.

Fisher's Station: Fisher's Station, also known as Carriage Point, was a stage stand on the old Butterfield Overland Mail route and the Texas Road in Indian Territory.  It was located at the head of Island Bayou in what is now Bryan County, Oklahoma.  Island Bayou was then the dividing line between the Chickasaw and Choctaw Nations.  From March 23, 1869, to February 6, 1871, the Carriage Point post office existed at the site and it is generally referred to by that name in the area.  The Fishers were a well known Choctaw family.

Klamath Tribes: The Klamath Tribes, formerly the Klamath Indian Tribe of Oregon, are a federally recognized Native American Nation consisting of three Native American tribes who traditionally inhabited Southern Oregon and Northern California in the United States: the Klamath, Modoc, and Yahooskin.  The tribal government is based in Chiloquin, Oregon.

United States Indian Police: The United States Indian Police (USIP) were organized in 1880 by John Q. Tufts the Indian Commissioner in Muskogee, Indian Territory, to police the Five Civilized Tribes.  Their mission is to "provide justice services and technical assistance to federally recognized Indian tribes."  The USIP, after its founding in 1880, recruited many of their police officers from the ranks of the existing Indian Lighthorsemen.  Unlike the Lighthorse who were under the direction of the individual tribe, the USIP was under the direction of the Indian agent assigned to the Union Agency.  Many of the US Indian police officers were given Deputy U.S. Marshal commissions that allowed them to cross jurisdictional boundaries and also to arrest non-Indians.

Lighthorse (American Indian police): Lighthorse (or Light Horse) was the name given by the Five Civilized Tribes of the United States to their mounted police force.  The Lighthorse were generally organized into companies and assigned to different districts.  Perhaps the most famous were the Cherokee Lighthorsemen which had their origins in Georgia.  Although the mounted police were disbanded when the Five Civilized Tribes lost their tribal lands in the late 19th century, some tribes still use the Lighthorse name for elements of their police forces.

Native American recognition in the United States: Native American (Indian) recognition in the United States most often refers to the process of a tribe being recognized by the United States federal government, or to a person being granted membership to a federally recognized tribe.  There are 567 federally recognized tribal governments in the United States.  Non-Acknowledged Tribes are tribes which have no federal designation as sovereign entities.  Federally Non-Recognized tribes refers to a subgroup of non-acknowledged tribes which had some sort of recognition by the British prior to the formation of the United States or by the United States but which were determined by the government to no longer exist as an Indian tribe or no longer meet the criteria for a nation to nation status.

Muscogee (Creek) Nation: The Muscogee (Creek) Nation is a federally recognized tribe of Muscogee people, also known as the Creek, based in the U.S. state of Oklahoma.  Calling themselves Este Mvskokvlke (] ), they are regarded as one of the historical Five Civilized Tribes of the American Southeast.  The tribe is descended from the historic Creek Confederacy, a large, heterogeneous group of indigenous peoples of the Southeastern Woodlands.

List of Native American actors: This is a list of Native American actors in the United States, including Alaskan Natives and American Indians. Native American identity is a complex and contested issue rooted in political sovereignty that pre-dates the creation of colonial nation states like the U.S. and Canada and persists into the 21st century recognized under international law by treaty.  The Bureau of Indian Affairs defines Native American as having American Indian or Alaska Native ancestry.  Legally, being Native American is defined as being enrolled in a federally recognized tribe or Alaskan village.  Ethnologically, factors such as culture, history, language, religion, and familial kinships can influence Native American identity.  All individuals on this list should have Native American ancestry.  Historical figures might predate tribal enrollment practices and would be included based on ethnological tribal membership, while any contemporary individuals should either be enrolled members of federally recognized tribes or have cited Native American ancestry and be recognized as being Native American by their respective tribes(s).  Contemporary unenrolled individuals are listed as being of descent from a tribe.

Five Civilized Tribes: The term "Five Civilized Tribes" derives from the colonial and early federal period in the history of the United States.  It refers to five Native American nations—the Cherokee, Chickasaw, Choctaw, Creek (Muscogee), and Seminole.  These are the first five tribes that Anglo-European settlers generally considered to be "civilized" according to their own worldview, because these five tribes adopted attributes of the colonists' culture, for example, Christianity, centralized governments, literacy, market participation, written constitutions, intermarriage with white Americans, and plantation slavery practices.  The Five Civilized Tribes tended to maintain stable political relations with the Europeans.

Chickasaw Nation: The Chickasaw Nation is a federally recognized Native American nation, located in Oklahoma.  They are one of the members of the Five Civilized Tribes.  The Chickasaw Nation was created after the Chickasaw people were forcibly removed by the US federal government to Indian Territory in the 1830s.  Their removal was part of a larger effort by the federal government to relocate Native American peoples from the eastern side of the Mississippi River; in the Southeast, these were the Cherokee, Muscogee (Creek), Seminole, Chickasaw, and Choctaw nations.  The removals became known as the "Trail of Tears".

Question: Which federally recognized Native American nation that Island Bayou was a dividing line, and is one of the members of the Five Civilized Tribes?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nation_name": {
      "type": "string",
      "description": "The name of the Native American nation."
    },
    "is_federally_recognized": {
      "type": "boolean",
      "description": "Indicates if the nation is federally recognized."
    },
    "is_five_civilized_tribe_member": {
      "type": "boolean",
      "description": "Indicates if the nation is a member of the Five Civilized Tribes."
    },
    "dividing_line_feature": {
      "type": "string",
      "description": "The geographical feature that served as a dividing line for the nation."
    },
    "other_nation_divided_by_feature": {
      "type": "string",
      "description": "The name of the other nation that shared the dividing line."
    }
  },
  "required": [
    "nation_name",
    "is_federally_recognized",
    "is_five_civilized_tribe_member",
    "dividing_line_feature",
    "other_nation_divided_by_feature"
  ],
  "additionalProperties": false
}
