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
Dean Oliver (statistician): Lawrence Dean Oliver (born February 6, 1969) is an American statistician who is prominent contributor to the statistical evaluation of basketball, sometimes called APBRmetrics after the forum of a growing community of basketball analysts.  He is the author of "Basketball on Paper", the former producer of the defunct Journal of Basketball Studies.  More recently, Oliver has served in front office roles with the Sacramento Kings, Seattle SuperSonics and Denver Nuggets of the NBA (including when the controversial trade for Allen Iverson was made).  In October 2015 Dean Oliver joined TruMedia Networks as Vice President of Data Science.  TruMedia Networks is an engineering firm specializing in sports analytics solutions for leagues, franchises and media partners, and says of Oliver in a press release announcing Dean Oliver's hiring, "Oliver was most recently in the front office of the Sacramento Kings and is considered one of the best minds in the world of sports analytics."

Maggie Koerth-Baker: Maggie Koerth-Baker (born 1981) is an American science journalist.  She is a senior science editor at "FiveThirtyEight" and was previously a science editor at "Boing Boing" and a monthly columnist for "The New York Times Magazine".  Koerth-Baker is the author of the 2012 book "Before the Lights Go Out: Conquering the Energy Crisis Before It Conquers Us".

Carl Bialik: Carl Bialik is an American journalist, who on February 6, 2017, was named Data Science Editor of Yelp, working on Yelpblog.  Prior to this, Bialik was known for his work for "The Wall Street Journal's" web site, and the paper itself.  He is also a co-founder of the growing online-only "Gelf Magazine".  In late 2013, Bialik was hired by Nate Silver at FiveThirtyEight.com.

Pete Palmer: Pete Palmer (born January 30, 1938) is an American sports statistician and encyclopedia editor.  He is a major contributor to the applied mathematical field referred to as sabermetrics.  Along with the Bill James "Baseball Abstracts", Palmer's book "The Hidden Game of Baseball" is often referred to as providing the foundation upon which the field of sabermetrics was built.

Cook's distance: In statistics, Cook's distance or Cook's "D" is a commonly used estimate of the influence of a data point when performing a least-squares regression analysis.  In a practical ordinary least squares analysis, Cook's distance can be used in several ways: to indicate influential data points that are particularly worth checking for validity; or to indicate regions of the design space where it would be good to be able to obtain more data points.  It is named after the American statistician R. Dennis Cook, who introduced the concept in 1977.

Data Science Africa: Data Science Africa (DSA) is a non-profit knowledge sharing professional group that aims at bringing together leading researchers and practitioners working on data science methods or applications relevant to Africa, and providing training on state of the art data science methods to students and others interested in developing practical skills.  Since 2013, DSA has been organizing conference, workshops and summer schools on machine learning and data science across East Africa.  Facilitators of Summer School and workshops are researchers and practitioners from the academia, private and public institutions across the world.

David Dunson: David Brian Dunson (born 1972) is an American statistician who is Arts and Sciences Distinguished Professor of Statistical Science, Mathematics and Electrical & Computer Engineering at Duke University.  His research focuses on developing innovative statistical methods for complex and high-dimensional data.  Particular themes of his work include the use of Bayesian hierarchical models, methods for learning latent structure in complex data, and the development of computationally efficient algorithms for uncertainty quantification.  He is currently serving as joint Editor of the Journal of the Royal Statistical Society Series B.

Daniel J. Bauer: Daniel John Bauer (born June 29, 1973) is an American statistician, professor, and director of the quantitative psychology program at the University of North Carolina, where he is also faculty at the Center for Developmental Science.  He is known for rigorous methodological work on latent variable models and is a proponent of "integrative data analysis", a meta-analytic technique that pools raw data across multiple independent studies.

Bill James: George William James (born October 5, 1949) is an American baseball writer, historian, and statistician whose work has been widely influential.  Since 1977, James has written more than two dozen books devoted to baseball history and statistics.  His approach, which he termed sabermetrics in reference to the Society for American Baseball Research (SABR), scientifically analyzes and studies baseball, often through the use of statistical data, in an attempt to determine why teams win and lose.  His "Baseball Abstract" books in the 1980s are the modern predecessor to websites using sabermetrics such as Baseball Prospectus and Baseball Primer (now Baseball Think Factory).

Nate Silver: Nathaniel Read Silver (born January 13, 1978) is an American statistician and writer who analyzes baseball (see sabermetrics) and elections (see psephology).  He is the editor-in-chief of ESPN's "FiveThirtyEight" and a Special Correspondent for ABC News.  Silver first gained public recognition for developing PECOTA, a system for forecasting the performance and career development of Major League Baseball players, which he sold to and then managed for Baseball Prospectus from 2003 to 2009.

Question: Carl Bialik is an American journalist, who on February 6, 2017, was named Data Science Editor of Yelp, working on Yelpblog, in late 2013, Bialik was hired by which American statistician and writer who analyzes baseball (see sabermetrics) and elections,at FiveThirtyEight.com?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_hired": {
      "type": "string",
      "description": "The name of the person who was hired."
    },
    "hiring_organization": {
      "type": "string",
      "description": "The organization where the hiring took place."
    },
    "hiring_date": {
      "type": "string",
      "description": "The approximate date of the hiring."
    },
    "hiring_manager": {
      "type": "object",
      "description": "Details about the person who did the hiring.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the hiring manager."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the hiring manager."
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of occupations of the hiring manager."
        },
        "analysis_fields": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Fields of analysis the hiring manager is known for."
        }
      },
      "required": [
        "name",
        "nationality",
        "occupations",
        "analysis_fields"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_hired",
    "hiring_organization",
    "hiring_date",
    "hiring_manager"
  ],
  "additionalProperties": false
}
