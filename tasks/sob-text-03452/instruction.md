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
Sue K. Hicks: Sue Kerr Hicks (December 12, 1895 – June 17, 1980) was an American jurist who practiced law and served as a circuit court judge in the state of Tennessee.  He is best known for his role as a co-instigator and prosecutor in the 1925 trial of John T. Scopes, a Dayton, Tennessee teacher accused of teaching the Theory of Evolution in violation of Tennessee state law.  Hicks may have also been the inspiration for the Shel Silverstein song "A Boy Named Sue," which was popularized by country music performer Johnny Cash in 1969.

Scopes Trial: The Scopes Trial, formally known as The State of Tennessee v. John Thomas Scopes and commonly referred to as the Scopes Monkey Trial, was an American legal case in July 1925 in which a substitute high school teacher, John T. Scopes, was accused of violating Tennessee's Butler Act, which had made it unlawful to teach human evolution in any state-funded school.  The trial was deliberately staged in order to attract publicity to the small town of Dayton, Tennessee, where it was held.  Scopes was unsure whether he had ever actually taught some evolution, but he purposely incriminated himself so that the case could have a defendant.

John T. Scopes: John Thomas Scopes (August 3, 1900 – October 21, 1970) was a teacher in Dayton, Tennessee, who was charged on May 5, 1925, with violating Tennessee's Butler Act, which prohibited the teaching of evolution in Tennessee schools.  He was tried in a case known as the Scopes Trial, in which he was found guilty and fined $100.

John Washington Butler: John Washington Butler (December 17, 1875 – September 24, 1952) was an American farmer and a member of the Tennessee House of Representatives from 1923-1927.  He is most noted for introducing the Butler Act, which prohibited teaching of evolution in public (i.e. state) schools (and which was challenged in the Scopes Trial).  He was an admirer of William Jennings Bryan.

Bryan College: Bryan College is a Christian liberal arts college in Dayton, Tennessee, United States.  It was founded in the aftermath of the 1925 Scopes Trial to establish an institution of higher education that would teach from a Christian worldview.

Civic Biology: A Civic Biology: Presented in Problems (usually referred to as just Civic Biology) was a biology textbook written by George William Hunter, published in 1914.  It is the book which the state of Tennessee required high school teachers to use in 1925 and is best known for its section about evolution that was ruled by a local court to be in violation of the state Butler Act.  It was for teaching from this textbook that John T. Scopes was brought to trial in Dayton, Tennessee in the Scopes "Monkey" Trial.  The views espoused in the book about evolution, race, and eugenics were common to American Progressives (especially in the work of Charles Benedict Davenport, one of the most prominent American biologists of the early 20th century, whom Hunter cites in the book).

George Rappleyea: George Washington Rappleyea (July 4, 1894 – August 29, 1966), an American metallurgical engineer and the manager of the Cumberland Coal and Iron Company in Dayton, Tennessee.  He held this position in the summer of 1925 when he became the chief architect of the Scopes Trial.  During a meeting at Robinson's Drug Store it was Rappleyea who convinced a group of Dayton businessmen to sponsor a test case of the Butler Act, which prohibited the teaching of evolution in the state's schools.  Rappleyea is held responsible for convincing John T. Scopes to be the defendant in the famous "Monkey" Trial.  (Note: The name is often spelled "Rappalyea" but the spelling "Rappleyea" is what appears in L. Sprague de Camp's book "The Great Monkey Trial" and the author interviewed Rappleyea before his death.)

Rhea County Courthouse: The Rhea County Courthouse is a historic county courthouse in the center of Dayton, the county seat of Rhea County, Tennessee.  Built in 1891, it is famous as the scene of the Scopes Trial of July 1925, in which teacher John T. Scopes faced charges for including Charles Darwin's theory of evolution in his public school lesson.  The trial became a clash of titans between the lawyers William Jennings Bryan for the prosecution and Clarence Darrow for the defense, and epitomizes the tension between fundamentalism and modernism in a wide range of aspects of American society.  The courthouse, now also housing a museum devoted to the trial, was designated a National Historic Landmark in 1976.

William Kinsey Hutchinson: William Kinsey "Bill" Hutchinson (June 27, 1896 – May 25, 1958) was an American reporter who became a friend of presidents, legislators, cabinet members, and other U.S. government diplomats and officials.  Between 1913 and 1920 William (Bill) worked as a reporter for a Reading, Pennsylvania newspaper.  He moved to Washington, D.C. in 1920 and started work for William Randolph Hearst's International News Service (INS).  As an INS reporter, he covered the John T. Scopes trial, also known as the Scopes Trial, in Dayton, Tennessee and on July 24, 1925 he was the first reporter to file the dispatch stating the outcome.  A conversation that occurred during the last days of the trial, Scopes said:

Monkey Town: Monkey Town: The Summer of the Scopes Trial is a 2006 novel written by American author Ronald Kidd.  The story is set in summer 1925 in Dayton, Tennessee, and is based on the Scopes Trial.

Question: George Washington Rappleyea, an American metallurgical engineer and the manager of the Cumberland Coal and Iron Company, in Dayton, Tennessee, he held this position in the summer of 1925, when he became the chief architect of the Scopes Trial, was an American legal case in July 1925, in which a substitute high school teacher, named what, was accused of violating Tennessee's Butler Act, which had made it unlawful to teach human evolution in any state-funded school?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "trial_details": {
      "type": "object",
      "properties": {
        "trial_name": {
          "type": "string",
          "description": "The formal or common name of the legal case."
        },
        "trial_date": {
          "type": "string",
          "description": "The month and year the trial took place."
        },
        "location": {
          "type": "string",
          "description": "The town and state where the trial was held."
        },
        "act_violated": {
          "type": "string",
          "description": "The name of the act or law that was allegedly violated."
        },
        "violation_description": {
          "type": "string",
          "description": "A description of what the act prohibited."
        }
      },
      "required": [
        "trial_name",
        "trial_date",
        "location",
        "act_violated",
        "violation_description"
      ],
      "additionalProperties": false
    },
    "accused_teacher": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the teacher accused in the trial."
        },
        "role": {
          "type": "string",
          "description": "The role of the accused person in the school."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "key_figure_rappleyea": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of George Washington Rappleyea."
        },
        "role_in_trial": {
          "type": "string",
          "description": "Rappleyea's primary role in initiating the trial."
        },
        "profession": {
          "type": "string",
          "description": "Rappleyea's professional occupation."
        },
        "company_managed": {
          "type": "string",
          "description": "The company Rappleyea managed at the time."
        },
        "location": {
          "type": "string",
          "description": "The town and state where Rappleyea held his position."
        }
      },
      "required": [
        "name",
        "role_in_trial",
        "profession",
        "company_managed",
        "location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "trial_details",
    "accused_teacher",
    "key_figure_rappleyea"
  ],
  "additionalProperties": false
}
