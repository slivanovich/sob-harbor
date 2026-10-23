{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEdith Roosevelt: Edith Kermit Carow Roosevelt (August 6, 1861 – September 30, 1948) was the second wife of President Theodore Roosevelt and served as First Lady of the United States during his presidency from 1901 to 1909.  She was the first First Lady to employ a full-time, salaried social secretary.  Her tenure resulted in the creation of an official staff, and her formal dinners and ceremonial processions served to elevate the position of First Lady.\n\nJulianna Smoot: Julianna Smoot is a political fundraiser for the Democratic Party.  She was a Deputy Manager of Barack Obama's 2012 presidential reelection campaign, having previously served as White House Social Secretary, Deputy Assistant to the President.  and Chief of Staff to United States Trade Representative Ron Kirk.  Smoot previously served as a professional fundraiser for the Democratic Party.  She was the national finance director for Obama's 2008 presidential campaign; under her direction, the campaign raised $32.5 million during the second quarter of 2007 and by election day, more money than any campaign in American history.  She was named Social Secretary after her predecessor, Desirée Rogers resigned on February 26, 2010.\n\nJacob Dolson Cox: Jacob Dolson Cox, (Jr.) (October 27, 1828August 4, 1900) was a statesman, lawyer, Union Army general during the American Civil War, and later a Republican politician from Ohio.  He served as the 28th Governor of Ohio and as United States Secretary of the Interior.  As Governor of Ohio, Cox sided for a time with President Andrew Johnson's Reconstruction plan and was against African American suffrage in the South, though he supported it in Ohio.  Seeing himself caught between Johnson and the Radical Republicans, Cox decided not to run for reelection.  He stayed out of politics for a year, though both Sherman and Grant advocated that Cox replace Stanton as Secretary of War as a means of stemming the demands for Johnson's impeachment.  But Johnson declined.  When Ulysses S. Grant became President he nominated Cox Secretary of Interior and Cox immediately accepted.  Secretary of Interior Cox implemented the first civil service reform in a federal government department, including examinations for most clerks.  Grant initially supported Cox and civil service reform, creating America's first Civil Service Commission.  However, Cox was opposed by Republican Party managers, who ultimately convinced Grant to cease civil service reforms.  President Grant and Secretary Cox were at odds over the fraudulent McGarahan Claims and the Dominican Republic annexation treaty.  Secretary Cox advocated a lasting, honest, and comprehensive Indian policy legislated by Congress after the Piegan Indian massacre.  Cox resigned as Secretary of Interior having been unable to gain Grant's support over civil service reform.  Although Cox was a reformer, Grant had believed Cox had overstepped his authority as Secretary of Interior and had undermined his authority as President.  In 1872 Cox joined the Liberal Republicans in opposition to Grant's renomination.  In 1876 Cox returned to politics and was elected to and served one term as United States Congressman of Ohio.  Congressman Cox supported President Hayes's reform efforts, but his term as Congressman was unsuccessful at establishing permanent Civil Service reform.  Cox retired and did not return to active politics, using his time to write several books on Civil War campaigns which remain today respected histories and memoirs.\n\nList of First Ladies of the United States: The First Lady of the United States is the hostess of the White House.  The position is traditionally filled by the wife of the President of the United States, but, on occasion, the title has been applied to women who were not presidents’ wives, such as when the president was a bachelor or widower, or when the wife of the president was unable to fulfill the duties of the First Lady herself.  The First Lady is not an elected position; it carries no official duties and receives no salary.  Nonetheless, she attends many official ceremonies and functions of state either along with or in place of the president.  Traditionally, the First Lady does not hold outside employment while occupying the office.  She has her own staff, including the White House Social Secretary, the Chief of Staff, the Press Secretary, the Chief Floral Designer, and the Executive Chef.  The Office of the First Lady is also in charge of all social and ceremonial events of the White House, and is a branch of the Executive Office of the President.\n\nJames P. Mitchell: James Paul Mitchell (November 12, 1900October 19, 1964) was an American politician and businessman from New Jersey.  Nicknamed \"the social conscience of the Republican Party,\" he served as United States Secretary of Labor from 1953 to 1961 during the Eisenhower Administration.  Mitchell was a potential running mate for the 1960 Republican presidential candidate, Vice President Richard M. Nixon.  However, Nixon chose Henry Cabot Lodge Jr.  After an unsuccessful run for Governor of New Jersey in 1961, he retired from politics.\n\nNancy Reagan: Nancy Davis Reagan (born Anne Frances Robbins; July 6, 1921 – March 6, 2016) was an American film actress and the wife of Ronald Reagan, the 40th President of the United States.  She served as the First Lady of the United States from 1981 to 1989.\n\nMalvina Thompson: Malvina \"Tommy\" Thompson (1893 - April 12, 1953) was a private secretary and personal aide to First Lady Eleanor Roosevelt.  She was a pioneer of the East Wing staff, being the first staffer for a First Lady of the United States who was not a social secretary.\n\nMuffie Cabot: Mabel \"Muffie\" Brandon Cabot (née Hobart; born c. 1936) is an American heiress and socialite.  During the 1980s she served as social secretary to Nancy Reagan.  She is the mother of Ali Wentworth, an actress notable for her appearances on the sketch comedy \"In Living Color\" and who is the wife of George Stephanopoulos.\n\nEast Wing: The East Wing is a part of the White House Complex.  It is a two-story structure east of the White House Executive Residence, the home of the President of the United States.  While the West Wing generally serves the president's executive office staff, the East Wing serves as office space for the First Lady and her staff, including the White House Social Secretary, White House Graphics and Calligraphy Office and correspondence staff.  The East Wing also includes the visitors' entrance, and the East Colonnade, a corridor connecting the body of the East Wing to the residence.  Along the corridor is also the White House theater, also called the Family theater.  Social visitors to the White House usually enter through the East Wing.\n\nWhite House Social Secretary: The White House Social Secretary is responsible for the planning, coordination and execution of official social events at the White House, the official residence and principal workplace of the President of the United States.\n\nQuestion: Muffie Cabot was the social secretary to an American film actress who was the wife of which president of the United States?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"social_secretary\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the social secretary.\"\n        },\n        \"tenure_period\": {\n          \"type\": \"string\",\n          \"description\": \"The period during which the social secretary served.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"tenure_period\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"first_lady\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the First Lady.\"\n        },\n        \"prior_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The prior profession of the First Lady.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"prior_profession\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"president\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the President.\"\n        },\n        \"presidency_years\": {\n          \"type\": \"string\",\n          \"description\": \"The years the president served.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"presidency_years\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"social_secretary\",\n    \"first_lady\",\n    \"president\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "social_secretary": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the social secretary."
          },
          "tenure_period": {
            "type": "string",
            "description": "The period during which the social secretary served."
          }
        },
        "required": [
          "name",
          "tenure_period"
        ],
        "additionalProperties": false
      },
      "first_lady": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the First Lady."
          },
          "prior_profession": {
            "type": "string",
            "description": "The prior profession of the First Lady."
          }
        },
        "required": [
          "name",
          "prior_profession"
        ],
        "additionalProperties": false
      },
      "president": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the President."
          },
          "presidency_years": {
            "type": "string",
            "description": "The years the president served."
          }
        },
        "required": [
          "name",
          "presidency_years"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "social_secretary",
      "first_lady",
      "president"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
