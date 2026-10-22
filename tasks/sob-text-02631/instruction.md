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
Henry Jenkins: Henry Jenkins III (born June 4, 1958) is an American media scholar and Provost Professor of Communication, Journalism, and Cinematic Arts, a joint professorship at the USC Annenberg School for Communication and Journalism and the USC School of Cinematic Arts.  He also has a joint faculty appointment with the USC Rossier School of Education.  Previously, Jenkins was the Peter de Florez Professor of Humanities as well as co-founder and co-director (with William Uricchio) of the Comparative Media Studies program at the Massachusetts Institute of Technology.  He has also served on the technical advisory board at ZeniMax Media, parent company of video game publisher Bethesda Softworks.  In 2013, he was appointed to the board that selects the prestigious Peabody Award winners.

Silvia Hagen: Silvia Hagen is an author who has published for O'Reilly Media on such topics as Internet Protocol version 6 in a book titled "IPv6 Essentials".  She lives in Switzerland.  In 2010, Silvia joined the BlueCat Networks Technical Advisory Board.  She has many years of experience in consulting enterprises in Europe and the US for the introduction of IPv6.  Since 2014 she engages in the agile community, co-founded the network flowdays and brings more and more agile elements in the complex task of IPv6 planning and deployment.

Microsoft: Microsoft Corporation ( , abbreviated as MS) is an American multinational technology company with headquarters in Redmond, Washington.  It develops, manufactures, licenses, supports and sells computer software, consumer electronics, personal computers, and services.  Its best known software products are the Microsoft Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers. Its flagship hardware products are the Xbox video game consoles and the Microsoft Surface tablet lineup.  As of 2016, it is the world's largest software maker by revenue, and one of the world's most valuable companies.  The word "Microsoft" is a portmanteau of "microcomputer" and "software".

Reza Zadeh: Reza Zadeh is a Canadian Computer Scientist working on Machine Learning.  He is adjunct professor at Stanford University and CEO at Matroid.  He has served on the technical advisory board of Microsoft and Databricks.

Jonathan M. Dorfan: Jonathan Manne Dorfan (born October 10, 1947) is a particle physicist and the former president of the Okinawa Institute of Science and Technology, Graduate University.  He is a former director of the Stanford Linear Accelerator Center (1999–2007; SLAC).  He received his B.Sc.  at the University of Cape Town in South Africa in 1969 and his Ph.D. from the University of California, Irvine in 1976.  Thereafter he worked on various projects at SLAC including MARK II and BaBar before becoming director in 1999.  He has served on numerous advisory boards, including the High Energy Physics Advisory Panel of the U.S. Department of Energy, the Scientific Advisory Board of the Max Planck Institute for Physics, the Board of Governors for the Weizmann Institute of Science, the Accelerator Advisory Panel of the International Linear Collider Global Design Effort, the Machine Advisory Committee for Italy's SuperB Project, the Advisory Board of the John Adams Institute for Accelerator Science, and the Board of Governors and Board of Councilors of the Okinawa Institute of Science and Technology.  

Schedule H: Schedule H is a class of prescription drugs in India appearing as an appendix to the Drugs and Cosmetics Rules, 1945 introduced in 1945.  These are drugs which cannot be purchased over the counter without the prescription of a qualified doctor.The manufacture and sale of all drugs are covered under the Drugs and Cosmetics Act and Rules.  It is revised at times based on the advice of the Drugs Technical Advisory Board, part of the Central Drugs Standard Control Organization in the Ministry of Health and Family Welfare.  The most recent schedule H (2006) lists 536 drugs from abacavir to zuclopenthixol.

Windmade: WindMade is a global (Brussel's based) consumer label for companies, events and products using wind power in their operations or production.  It is aimed at promoting wind power and is guided by a Technical Advisory Board, which includes various scientists, and third-party auditors.  The organization is a non-profit NGO established by seven Founding Partners: United Nations Global Compact, WWF, Global Wind Energy Council, LEGO Group, PricewaterhouseCoopers (PwC), Bloomberg L.P. and Vestas Wind Systems.

Dyesol: DSC technology was invented at the Institute of Physical Chemistry, Swiss Federal Institute of Technology in Lausanne, Switzerland in 1988 by Brian O'Regan and Michael Graetzel.  Their paper A low-cost, high-efficiency solar cell based on dye-sensitized colloidal TiO films, published in 1991 in the journal, "Nature", was the catalyst that spawned a whole new industry and a whole new way of looking at harvesting electrical power from sunlight.  Since that time Professor Graetzel, now at Switzerland's École Polytechnique Fédérale de Lausanne (EPFL), has remained strongly focused on DSC technology, received numerous awards and accolades in relation to the invention of DSC, and maintained close links to Dyesol as Chairman of Dyesol's Technical Advisory Board.

Cruzential: Cruzential is the second album from the Danish band Kashmir.  The producer and engineer Ron Saint Germain used the two words ‘crucial’ and ‘essential’ constantly, and the title of the album is a portmanteau of the two words.

Rachel Jewkes: Rachel Jewkes is Unit Director of the Gender and Health Unit of the Medical Research Council, based in Pretoria, South Africa, and a member of the National Council Against Gender-Based Violence in South Africa.  Jewkes studied Medicine, receiving a Masters in Community Medicine (MSc) and a Doctorate in Medicine (MD) from the London School of Hygiene & Tropical Medicine, University of London.  She is an Honorary Professor in the faculty of Health Sciences, School of Public Health at the University of Witwatersrand, Johannesburg.  Jewkes is the Secretary of the Sexual Violence Research Initiative and a regional member of the WHO Expert Advisory Panel on Injury and Violence Prevention and Control.  She is a member of the PEPFAR Scientific Advisory Board and the WHO's Strategic and Technical Advisory Committee for HIV-AIDS (STAC-HIV).  Jewkes moved from England to South Africa in 1994.

Question: Reza Zadeh has served on the technical advisory board of a company whose name is a portmanteau of what two words?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who served on the technical advisory board."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the company whose technical advisory board the person served on."
    },
    "is_portmanteau": {
      "type": "boolean",
      "description": "Indicates if the company's name is a portmanteau."
    },
    "portmanteau_words": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The two words that form the portmanteau name of the company."
    }
  },
  "required": [
    "person_name",
    "company_name",
    "is_portmanteau",
    "portmanteau_words"
  ],
  "additionalProperties": false
}
