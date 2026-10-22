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
New Jersey Farm Winery Act: The New Jersey Farm Winery Act was legislation passed by the New Jersey state legislature and signed by Governor Brendan Byrne in 1981.  The Farm Winery Act was the first of several efforts by the New Jersey state legislature to relax Prohibition-era restrictions and craft new laws to facilitate the growth of the alcoholic beverage industry and provide new opportunities for winery licenses.  Before it was enacted, New Jersey provided only one winery license for each million residents and licenses were practically impossible to obtain.  By 1981, New Jersey boasted only seven wineries.  By 1988, that number had doubled to 15.  s of 2014 , New Jersey currently has 48 licensed and operating wineries with several more prospective wineries in various stages of development.  New Jersey wineries produce wine from more than 90 varieties of grapes, and from over 25 other fruits.

Augustinians: The term Augustinians, named after Augustine of Hippo (354–430), applies to two distinct types of Catholic religious orders and some Anglican religious orders. Within Anglicanism the Rule of St. Augustine is followed only by women, who form several different communities of Augustinian nuns in the Anglican Communion.  Within Roman Catholicism Augustinians may be members of either one of two separate and distinct types of Order:

Michigan wine: Michigan wine refers to any wine that is made in the state of Michigan in the United States.  As of 2013, there were 2650 acre under wine-grape cultivation and 101 commercial wineries in Michigan, producing 1.3 e6USgal of wine.  According to another count there were 112 operating wineries in Michigan in 2007.

Alcohol laws of New Jersey: The state laws governing alcoholic beverages in New Jersey are among the most complex in the United States, with many peculiarities not found in other states' laws.  They provide for 29 distinct liquor licenses granted to manufacturers, wholesalers, retailers, and for the public warehousing and transport of alcoholic beverages.  General authority for the statutory and regulatory control of alcoholic beverages rests with the state government, particularly the Division of Alcoholic Beverage Control overseen by the state's Attorney General.

Liquor Control and Licensing Branch: The Liquor Control and Licensing Branch is part of the government of British Columbia, within the Ministry of Small Business and Red Tape Reduction.  It is responsible for issuing liquor licenses in the province and for enforcing the provisions of the "Liquor Control and Licensing Act".

New Mexico Alcohol and Gaming Division: The Alcohol and Gaming Division is a division of the New Mexico Regulation and Licensing Department.  It administers the licensing provisions, while the Special Investigations Division of the Department of Public Safety enforces the prouvisions of the New Mexico Liquor Control Act.  The Alcohol and Gaming Division processes applications for New Mexico Liquor Licenses, supervises the state’s Alcohol Server Training program, and adjudicates administrative citations for violation of the Liquor Control Act.

New Jersey Wine Industry Advisory Council: New Jersey is home to the most complex alcohol laws in the United States.  They provide 29 liquor licenses to wholesalers, manufacturers, retailers and the general public.

Oregon Ballot Measure 7 (1940): Oregon Ballot Mesure 7 (1940) was an initiative proposed for the general election on the November 5, 1940, ballot to repeal the present liquor law, and allow private sales, with regulation and tax.  The official ballot title states its intention as "BILL REPEALING PRESENT LIQUOR LAW; AUTHORIZING PRIVATE SALE, LICENSED, TAXED."  It was defeated with 309,183 no votes, to only 90,681 votes in favor.  After the repeal of prohibition by the Twenty-first Amendment to the United States Constitution on December 5, 1933, the Oregon Liquor Control Commission (OLCC) was established to regulate and control the sales and consumption of alcoholic liquor in Oregon.  At the time, the law stated that: "only the liquor control commission can import, purchase and sell alcoholic liquor containing over seventeen percent of alcohol, and that such liquor may not be consumed on the premises".  The ballot measure attempted to ratify the OLCC's dominance of liquor and "permit liquor being consumed both on and off the premises where sold, depending on vendor's license."  The commission, according to the proposed bill, was to issue numerous classes of wholesale and retail liquor licenses, while "levying privileges of sales taxes on the various classes of liquor business".

New Jersey wine: The production of wine in New Jersey has increased significantly in the last thirty years with opening of new wineries.  Beginning in 1981, the state legislature relaxed Prohibition-era restrictions and crafted new laws to facilitate the growth of the industry and provide new opportunities for winery licenses.  Today, New Jersey wineries are crafting wines that have earned recognition for their quality from critics, industry leaders, and in national and international competitions.  s of 2014 , New Jersey currently has 48 licensed and operating wineries with several more prospective wineries in various stages of development.

Arizona Department of Liquor Licenses and Control: The Department of Liquor Licenses and Control is an Arizona state agency responsible for reviewing state liquor applications and issuing renewal licenses.  In Arizona, there are 17 different license categories – airplanes, trains, watercraft, restaurants, liquor stores and other retailers, hotels, bars, distillers, distributors, and special events.

Question: Which state has 29 distinct types of liquor licenses and 48 operating wineries?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "state_name": {
      "type": "string",
      "description": "The name of the state."
    },
    "number_of_liquor_licenses": {
      "type": "integer",
      "description": "The number of distinct liquor licenses provided by the state."
    },
    "number_of_operating_wineries": {
      "type": "integer",
      "description": "The number of licensed and operating wineries in the state."
    },
    "winery_count_as_of_year": {
      "type": "integer",
      "description": "The year for which the winery count is valid."
    }
  },
  "required": [
    "state_name",
    "number_of_liquor_licenses",
    "number_of_operating_wineries",
    "winery_count_as_of_year"
  ],
  "additionalProperties": false
}
