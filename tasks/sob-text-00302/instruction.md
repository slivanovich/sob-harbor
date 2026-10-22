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
University of Saskatchewan: The University of Saskatchewan (U of S) is a Canadian public research university, founded in 1907, and located on the east side of the South Saskatchewan River in Saskatoon, Saskatchewan, Canada.  An "Act to establish and incorporate a University for the Province of Saskatchewan" was passed by the provincial legislature in 1907.  It established the provincial university on April 3, 1907 "for the purpose of providing facilities for higher education in all its branches and enabling all persons without regard to race, creed or religion to take the fullest advantage".  The University of Saskatchewan is the largest education institution in the Canadian province of Saskatchewan.  The University of Saskatchewan is one of Canada’s top research universities (based on the number of Canada Research Chairs) and is a member of the U15 Group of Canadian Research Universities (the 15 most research-intensive universities in Canada).

Dermot Moran: Dermot Moran ( ) is an Irish philosopher specialising in phenomenology and in medieval philosophy and also active in the dialogue between analytic and continental philosophy.  He is currently Professor of Philosophy (Metaphysics and Logic) at University College Dublin.  He previously taught at St. Patrick's College, Maynooth, Queen's University of Belfast, and Yale University.  He has served as a visiting professor of philosophy in many universities around the world, including Rice University, Sorbonne, University at Albany, SUNY, Catholic University of Leuven, Trinity College Dublin, Connecticut College, Ludwig Maximilian University of Munich and Northwestern University.  He has been an elected member of the Royal Irish Academy since March 2003 and has been involved in the Fédération Internationale des Sociétés de Philosophie, the highest non-governmental world organisation for philosophy, since the 1980s.  He is the Founding Editor of International Journal of Philosophical Studies, founded in 1993 and published by Routledge, and co-editor of Contributions To Phenomenology book series, published by Springer.  His monograph Introduction to Phenomenology was awarded the Edward Goodwin Ballard Prize in Phenomenology (2001) and was translated into Chinese.  A Turkish translation of the book is in preparation.  Moran has also been elected President of the Programme Committee for the 23rd World Congress of Philosophy which took place in Athens from 4–10 August 2013.

International Research Universities Network: The International Research Universities Network (IRUN), initiated in 2006 by Radboud University Nijmegen in the Netherlands, was officially founded during a meeting in September 2007 in Nijmegen.  Representatives from each of the network’s nine founding partner universities signed the IRUN Charter.  IRUN currently represents eight European countries and is expected to grow in numbers of universities, countries and world regions represented.  All universities currently in the network are research universities: their teaching efforts are predicated on the vigour and quality of their own research programmes and recent international scientific developments.  It is the goal of IRUN that all research produced by the partners is pioneering and innovative.

Emory University: Emory University is a private research university in metropolitan Atlanta, located in the Druid Hills section of DeKalb County, Georgia, United States.  The university was founded as Emory College in 1836 in Oxford, Georgia by the Methodist Episcopal Church and was named in honor of Methodist bishop John Emory.  In 1915, the college relocated to metropolitan Atlanta and was rechartered as Emory University.  The university is the second-oldest private institution of higher education in Georgia and among the fifty oldest private universities in the United States.  Emory is frequently cited as one of the world's leading research universities and one of the top institutions in the United States.

Research university: A research university is a university that expects all its tenured and tenure-track faculty to continuously engage in research, as opposed to merely requiring it as a condition of an initial appointment or tenure.  Such universities can be recognized by their strong focus on innovative research and the prestige of their brand names.  On the one hand, research universities strive to recruit faculty who are the most brilliant minds in their disciplines in the world, and their students in theory enjoy the opportunity to learn from such experts.  On the other hand, new students are often disappointed to realize their undergraduate courses at research universities are overly academic and fail to provide vocational training with immediate "real world" applications; but many employers value degrees from research universities because they know that such coursework develops fundamental skills like critical thinking.

Woodson Research Center: Woodson Research Center is an archive located in the Fondren Library of Rice University in Houston, Texas.  The Center is named for Benjamin N. Woodson and houses the special collections of Rice University's Fondren Library which includes rare books, manuscripts, and the Rice University archives.

Yale University: Yale University is an American private Ivy League research university in New Haven, Connecticut.  Founded in 1701, it is the third-oldest institution of higher education in the United States and one of the nine Colonial Colleges chartered before the American Revolution.

Hanyang University: Hanyang University is one of the leading private research universities of South Korea, especially in the field of engineering.  The main campus is in Seoul, and its branch, the Education Research Industry Cluster at Ansan, or ERICA campus, is located in Ansan.  "Hanyang" (한양;漢陽) derives from the former name of the capital Seoul used during the Chosun Dynasty.  The university was established as an engineering institute (DongA Engineering Institute) in 1939, and became the founding facility of Hanyang University with its motto and educational philosophy of "Love in Deed and Truth".  Hanyang University enrolls over 2,000 foreign students each year and more than 3,000 students study abroad annually, and counts its 647 partner universities in 68 countries.

Rice University: Rice University, officially William Marsh Rice University, is a private research university located on a 295-acre campus in Houston, Texas, United States.  The university is situated near the Houston Museum District and is adjacent to the Texas Medical Center.  Rice is generally considered the top university and the most selective institution of higher education in the state of Texas.

Jesse H. Jones Graduate School of Business: Located on a 285-acre wooded campus, The Jesse H. Jones Graduate School of Business is the business school of Rice University in Houston, Texas.  Named in honor of Jesse Holman Jones, a Houston business and civic leader, the school received its initial funding in 1974 through a major gift from the Houston Endowment Inc., a philanthropic foundation established by Jones and his wife, Mary Gibbs Jones.  The Jones School is distinguished by its foundation in accounting, finance, marketing, organizational behavior and management with areas of excellence in energy, entrepreneurship and health care.  Degree programs include the Rice Master of Business Administration (MBA), MBA for Executives, and MBA for Professionals.  In addition, the school offers several joint degree programs, including the MD/MBA with Baylor College of Medicine, MBA/ME with Rice’s George R. Brown School of Engineering, and MBA/MS with Rice’s Wiess School of Natural Sciences.  A Ph.D. in Business — in marketing, finance, strategic management, and accounting — attracts candidates aspiring to become faculty at business schools in prestigious research universities internationally.  The Jones School also provides an undergraduate business minor and full schedule of non-credit executive education open enrollment and customized courses for business and industry, along with certificates in finance and accounting, health care, and marketing.

Question: Yale University and Rice University, are private research universities, located in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "universities_info": {
      "type": "array",
      "description": "Information about each university mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "university_name": {
            "type": "string",
            "description": "The name of the university."
          },
          "university_type": {
            "type": "string",
            "description": "The type of the university, e.g., 'private research university'."
          },
          "country": {
            "type": "string",
            "description": "The country where the university is located."
          }
        },
        "required": [
          "university_name",
          "university_type",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "shared_country": {
      "type": "string",
      "description": "The country where all specified universities are located."
    },
    "all_are_private_research_universities": {
      "type": "boolean",
      "description": "Indicates if all listed universities are private research universities."
    }
  },
  "required": [
    "universities_info",
    "shared_country",
    "all_are_private_research_universities"
  ],
  "additionalProperties": false
}
