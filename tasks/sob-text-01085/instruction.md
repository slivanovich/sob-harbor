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
IMANI Centre for Policy and Education: The '"IMANI Center for Policy and Education"' is an African think tank based in Accra, Ghana.  As a member of the Atlas Economic Research Foundation, the think tank applies free market solutions to intricate domestic social problems.  It was founded in 2004 by Franklin Cudjoe, who currently serves as the president and chief executive officer.  The think tank's operations center on these four thematic areas: rule of law, market growth and development, individual rights, and human security and institutional development.  IMANI uses the Africanliberty.org platform as a springboard to reach out to the larger African audience in five international languages, including Swahili.IMANI exerts influence in the Ghanaian public education and policy sphere through media appearances, publications, research, and seminars.  The think tank is ranked by the Global Go To Think Tanks and Civil Societies Program, organized annually by the University of Pennsylvania.  According to the 2009 Index Report, IMANI was ranked fifth most influential in Sub-Saharan Africa, and the only African think tank to make the list of top 25 "Most Innovative" across the world.

Mikhail Voloshin: Mikhail "Misha" Voloshin (born 1953) is a Russian and American theoretical physicist.  Voloshin started working at ITEP in 1976 and accordingly earned his Ph.D. in 1977.  In 1983 he received a Soviet medal and an award in physics.  Since 1990 he started at the William I Fine Theoretical Physics Institute, University of Minnesota, a division of the University of Minnesota College of Science and Engineering where he teaches quantum physics.  In 1997 elected a fellow of the American Physical Society.  In 2001 he was awarded J.J. Sakurai Prize for Theoretical Particle Physics and in 2004 he was awarded the Alexander-von-Humboldt Award.

Avi Loeb: Abraham (Avi) Loeb is an American theoretical physicist who works on astrophysics and cosmology.  Loeb is the "Frank B. Baird Jr.  Professor of Science" at Harvard University.  He serves as Chair of the "Harvard Astronomy department", Chair of the Advisory Committee for the "Breakthrough Starshot" project - which aims to launch lightweight spacecraft towards the nearest stars using a powerful laser, founding director of Harvard's "Black Hole Initiative" - the first interdisciplinary center worldwide dedicated to the study of black holes and director of the "Institute for Theory and Computation (ITC)" within the Harvard-Smithsonian Center for Astrophysics.  Loeb is an elected fellow of the American Academy of Arts and Sciences, the American Physical Society, and the International Academy of Astronautics, as well as Vice Chair of the Board on Physics and Astronomy of the National Academies.  Within Harvard, Loeb serves on the President's Task Force on Diversity and Belonging, the Provost's Allston Academic Planning Committee, and the FAS Dean's Faculty Resources Advisory Committee.  In December 2012, "TIME" magazine selected Loeb as one of the 25 most influential people in space.  In 2015, Loeb was appointed as the Science Theory Director for the Breakthrough Initiatives of the Breakthrough Prize Foundation.

Lisa Randall: Lisa Randall (born June 18, 1962) is an American theoretical physicist working in particle physics and cosmology.  She is the Frank B. Baird, Jr.  Professor of Science on the physics faculty of Harvard University.  Her research includes elementary particles, fundamental forces and extra dimensions of space.  She studies the Standard Model, supersymmetry, possible solutions to the hierarchy problem concerning the relative weakness of gravity, cosmology of extra dimensions, baryogenesis, cosmological inflation, and dark matter.  She contributed to the Randall–Sundrum model, first published in 1999 with Raman Sundrum.

James A. Baker III Institute for Public Policy: The James A. Baker III Institute for Public Policy, also known as the Baker Institute, is an American think tank on the campus of Rice University in Houston, Texas.  Founded in 1993, it functions as a nonpartisan center for public policy research.  According to the "2015 Global Go To Think Tank Index Report" (Think Tanks and Civil Societies Program, University of Pennsylvania), the institute is No. 18 (of 60) in the "Top Think Tanks in the United States" and No. 4 (of 45) of the "Best University Affiliated Thanks".  Its Center for Energy Studies is ranked No. 2 (of 55) among the world’s energy- and resource-policy think tanks, according to the Think Tanks and Civil Societies Program’s 2015 Index Report.  It is named for James A. Baker, III, former United States secretary of state and secretary of the Treasury.  The institute's director Edward P. Djerejian is the former United States ambassador to Israel and Syria and assistant secretary of state for Near Eastern Affairs.  The institute's board of advisors include William Barnett (Chair), Colin Powell, Madeleine Albright and Rice University's President David Leebron.

Libertad y Desarrollo: Libertad y Desarrollo, abbreviated to LyD, is a Chilean think tank focused on liberal, free market economic studies.  Founded in 1990, the think tank defines itself as a "center for studies and private research, independent of any political, religious, business, or governmental organization, that is dedicated to the analysis of public affairs promoting the values and principles of a free society".  The think tank is the Chilean representative of RELIAL, the Liberal Network of Latin America ("Red Liberal de America Latina").  The center is divided into 7 programs: Economic Program, Social Program, Society and Politics Program, Legislative Program, Environmental Program, and the Justice Program.  The group's goal is to respond to these various issues with a liberal, free market perspective and to make public policy recommendations specific to Chile for legislators, but not to participate in government directly.  Economists Hernan Büchi, Luis Larraín, Cristián Larroulet are affiliated with the think tank.

Point of Inquiry: Point of Inquiry is the radio show and flagship podcast of the Center for Inquiry (CFI), "a think tank promoting science, reason, and secular values in public policy and at the grass roots".  Started in 2005, "Point of Inquiry" has consistently been ranked among the best science podcasts available in iTunes.  It has been celebrated for its guests and for the quality of its interviews.  Former guests include leading scientists, writers and public intellectuals such as Neil DeGrasse Tyson, Paul Krugman, Lisa Randall, Brian Greene, Oliver Sacks, Susan Jacoby, David Brin and Temple Grandin.

Brian Lee Crowley: Brian Lee Crowley, a native of Vancouver, British Columbia, Canada, is Managing Director of the Macdonald-Laurier Institute, a national public policy think tank based in Ottawa, Ontario, Canada.  He was also the founding President of the Atlantic Institute for Market Studies (AIMS), a public policy think tank based in Atlantic Canada.  He authored of three books ("The Self, the Individual and the Community", Oxford University Press, 1987; "The Road to Equity: Impolitic Essays", Stoddart, 1994; and "Fearful Symmetry: The Fall and Rise of Canada’s Founding Values", Key Porter Books, 2009).  He was the editor of "Taking Ownership: Property Rights and Fishery Management on the Atlantic Coast", AIMS, 1996.

Matthew Kleban: Matthew Benjamin Kleban is an American theoretical physicist who works on string theory and theoretical cosmology.  He is an associate professor at New York University, a member of the Center for Cosmology and Particle Physics, and a former member at the Institute for Advanced Study.  His contributions to physics include:

Information Technology and Innovation Foundation: The Information Technology and Innovation Foundation (ITIF) is a U.S. nonprofit public policy think tank based out of Washington, D.C. The organization focuses on public policies that spur technology innovation.  The University of Pennsylvania rates ITIF the most authoritative science and technology think tank in the United States, and the second most authoritative science and technology think tank in the world, behind Germany's Max Planck Institutes.  Ars Technica has described ITIF as "one of the leading, and most prolific, tech policy think tanks."

Question: An American theoretical physicist who worked in particle physics and cosmology, she was also known as the Frank B. Baird, Jr., was a former guest on a podcast that was described as "a think tank promoting science, reason, and secular values in public policy and at the grass roots"; when was that podcast started?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the theoretical physicist."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the physicist."
        },
        "field_of_work": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The areas of physics the person works in."
        },
        "academic_position": {
          "type": "string",
          "description": "The academic position held by the physicist."
        }
      },
      "required": [
        "name",
        "nationality",
        "field_of_work",
        "academic_position"
      ],
      "additionalProperties": false
    },
    "podcast": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the podcast."
        },
        "start_year": {
          "type": "integer",
          "description": "The year the podcast started."
        },
        "description": {
          "type": "string",
          "description": "A description of the podcast's focus."
        }
      },
      "required": [
        "name",
        "start_year",
        "description"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "string",
      "description": "Describes the relationship between the person and the podcast."
    }
  },
  "required": [
    "person",
    "podcast",
    "relationship"
  ],
  "additionalProperties": false
}
