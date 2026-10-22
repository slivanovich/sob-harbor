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
Johannes Juilfs: Johannes Wilhelm Heinrich Juilfs, also known by the alias Mathias Jules, (15 December 1911 – 1995) was a German theoretical and experimental physicist.  He was a member of the "Sturmabteilung" (SA) and then, in 1933, of the "Schutzstaffel" (SS).  Prior to World War II, he was one of three SS staff physicists who investigated the physicist Werner Heisenberg during the Heisenberg Affair, instigated, in part, by the ideological "deutsche Physik" (German physics) movement.  During the war, he worked as a theoretical physics assistant at the Kaiser Wilhelm Institute for Physics.  During the denazification process after World War II, he was banned from working as a civil servant in academia.  For a few years, he worked as a school principal, and then he took a job as a physicist in the textile industry.  With the help of Heisenberg and the Minister of Lower Saxony, he was able to become a full professor at the University of Hanover.

Fundamentals of Physics: Fundamentals of Physics is a calculus-based physics textbook by David Halliday, Robert Resnick, and Jearl Walker.  The textbook is currently in its tenth edition (published 2013).  The current version is a revised version of the original 1960 textbook "Physics for Students of Science and Engineering" by Halliday and Resnick, which was published in two parts (Part I containing Chapters 1-25 and covering mechanics and thermodynamics; Part II containing Chapters 26-48 and covering electromagnetism, optics, and introducing quantum physics).  A 1966 revision of the first edition of Part I changed the title of the textbook to "Physics".  It is widely used in colleges as part of the undergraduate physics courses, and has been well known to science and engineering students for decades as "the gold standard" of freshman-level physics texts.  In 2002, the American Physical Society named the work the most outstanding introductory physics text of the 20th century.

Erich Schumann: Erich Schumann (5 January 1898 – 25 April 1985) was a German physicist who specialized in acoustics and explosives, and had a penchant for music.  He was a general officer in the army and a professor at the University of Berlin and the Technical University of Berlin.  When Adolf Hitler came to power he joined the Nazi Party.  During World War II, his positions in the Army Ordnance Office and the Army High Command made him one of the most powerful and influential physicists in Germany.  He ran the German nuclear energy program from 1939 to 1942, when the army relinquished control to the Reich Research Council.  His role in the project was obfuscated after the war by the German physics community’s defense of its conduct during the war.  The publication of his book on the military’s role in the project was not allowed by the British occupation authorities.  He was director of the Helmholtz Institute of Sound Psychology and Medical Acoustics.

Philipp Lenard: Philipp Eduard Anton von Lenard (7 June 1862 – 20 May 1947) was a German physicist and the winner of the Nobel Prize for Physics in 1905 for his research on cathode rays and the discovery of many of their properties.  He was a nationalist and anti-Semite; as an active proponent of the Nazi ideology, he had supported Adolf Hitler in the 1920s and was an important role model for the "Deutsche Physik" movement during the Nazi period.  Notably, he had labeled Albert Einstein's contributions to science as constituting "Jewish physics".

Palash Baran Pal: Palash Baran Pal (Bengali: পলাশ বরন পাল "Palāś Baran Pāl", born : 1955) is an Indian theoretical physicist, a senior professor at Saha Institute of Nuclear Physics, Kolkata, a writer, a linguist and a poet.  His main area of research is Particle Physics.  His works in the area of neutrino physics and relativistic treatment of particle properties in matter are well recognized in the particle physics community.  Apart from his scientific contributions, he has authored well known text books in physics as well as several popular science literature in Bengali to popularize science.

Hugh D. Young: Hugh David Young (November 3, 1930 – August 20, 2013) was an American physicist who taught physics for 52 years at Carnegie Mellon University.  Young is best known for co-authoring the later editions of "University Physics", a highly regarded introductory physics textbook, with Francis Sears and Mark Zemansky (this book - first published in 1949 - is often referred to as ""Sears and Zemansky"", although Hugh Young became a coauthor in 1973).

John D. Strong: John Donovan Strong was a professor of Physics and Astronomy from 1967 to 1975 and served as the head of the laboratory of astrophysics and physical meteorology.  Strong, one of the world’s foremost optical scientists, was known for being the first to detect water vapor in the atmosphere of Venus and for developing a number of innovations in optical devices, ranging from improved telescope mirrors to anti-reflective coatings for optical elements and diffraction gratings.  Born in Lawrence, Kansas in 1905, Strong received degrees from the University of Kansas (BA 1926) and the University of Michigan (M.S., 1928, Ph.D., 1930).  After twelve years at Caltech and wartime research at Harvard on infrared systems, Strong became professor and director of the Astrophysics and Physical Meteorology Laboratories at Johns Hopkins University in 1946, where, among many other projects, he conducted research on balloon astronomy for the Office of Naval Research (ONR).  Strong published hundreds of papers throughout his career and was author of Procedures in Experimental Physics, a standard physics textbook for many years.  Strong served as president of the American Optical Association in 1959 and patented numerous inventions for optics in spectroscopy as well as golf (see US Patent no. 3720467).  Strong died in 1992.

Cathode ray: Cathode rays (also called an electron beam or e-beam) are streams of electrons observed in vacuum tubes.  If an evacuated glass tube is equipped with two electrodes and a voltage is applied, the glass behind of the positive electrode is observed to glow, due to electrons emitted from and traveling away from the cathode (the electrode connected to the negative terminal of the voltage supply).  They were first observed in 1869 by German physicist Johann Wilhelm Hittorf, and were named in 1876 by Eugen Goldstein "Kathodenstrahlen", or cathode rays.

Deutsche Physik: Deutsche Physik (literally: "German Physics") or Aryan Physics (German: "Arische Physik" ) was a nationalist movement in the German physics community in the early 1930s.  A pseudoscientific movement, it nonetheless won the support of many eminent physicists in Germany.  The term was taken from the title of a 4-volume physics textbook by Nobel Laureate Philipp Lenard in the 1930s.

Johannes Stark: Johannes Stark (] , 15 April 1874 – 21 June 1957) was a German physicist and Physics Nobel Prize laureate.  He is known for identifying the Stark effect, and was later closely involved with the "Deutsche Physik" movement under the Nazi regime.

Question: Deutsche Physik, was a nationalist movement in the German physics community in the early 1930s, the term was taken from the title of a 4-volume physics textbook, in the 1930s by who, which was a German physicist and the winner of the Nobel Prize for Physics in 1905 for his research on cathode rays and the discovery of many of their properties?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movement_name": {
      "type": "string",
      "description": "The name of the nationalist physics movement."
    },
    "textbook_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the textbook from which the movement's name was taken."
        },
        "number_of_volumes": {
          "type": "integer",
          "description": "The number of volumes in the textbook."
        },
        "publication_decade": {
          "type": "string",
          "description": "The decade in which the textbook was published."
        }
      },
      "required": [
        "title",
        "number_of_volumes",
        "publication_decade"
      ],
      "additionalProperties": false
    },
    "author_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the author of the textbook."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the author."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the author."
        },
        "nobel_prize_winner": {
          "type": "boolean",
          "description": "Indicates if the author was a Nobel Prize winner."
        },
        "nobel_prize_year": {
          "type": "integer",
          "description": "The year the author won the Nobel Prize."
        },
        "nobel_prize_reason": {
          "type": "string",
          "description": "The reason for which the author won the Nobel Prize."
        }
      },
      "required": [
        "name",
        "nationality",
        "profession",
        "nobel_prize_winner",
        "nobel_prize_year",
        "nobel_prize_reason"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movement_name",
    "textbook_details",
    "author_details"
  ],
  "additionalProperties": false
}
