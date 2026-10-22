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
Protective Life: Protective Life Corporation is a financial service holding company in Birmingham, Alabama.  The company’s primary subsidiary, Protective Life Insurance Company, was established in 1907 and now markets its products and services in all 50 states.  As of December 31, 2016, the corporation had more than 2,700 employees, annual revenues of $4.48 billion and assets of $75 billion.  In addition to Protective Life Insurance Company, Protective Life Corporation's subsidiaries include West Coast Life Insurance Company, MONY Life Insurance Company, Protective Life And Annuity Insurance Company, ProEquities Inc./Protective Securities, and Lyndon Property Insurance Company.

Southern Aid and Insurance Company: The Southern Aid and Insurance Company is an insurance company that was founded in 1893, just 28 years after the end of the Civil War, by a group of black men (American men of African ancestry) in Richmond, Virginia.  The purpose was to furnish adequate and affordable insurance protection to African-Americans.  The company was the first chartered insurance company organized by blacks in the United States and had the distinction of being the oldest black owned and operated insurance company in the nation.  It was also the largest African-American insurance company in the United States at one time.  The company's name was later changed to the Southern Aid Society of Virginia which was the forerunner of the Southern Aid Life Insurance Company.

Norwich Union: Norwich Union was the name of insurance company Aviva's British arm before June 2009.  It was originally established in 1797.  It was listed on the London Stock Exchange and was once a constituent of the FTSE 100 Index.

Economical Insurance: Economical Insurance, founded in 1871, is a Canadian Property & Casualty insurance company, offering automobile, property, liability, agriculture, and surety insurance.  Its executive offices are located in Waterloo, Ontario, with regional offices across Canada.  The company has a 4.02% market share, measured by direct written premium in the Canadian Property & Casualty Insurance market as of December 2012. As of 2014, it had about 1.6 billion in mutual policyholder's equity.  It is the 9th largest property and casualty insurance company in Canada, by direct written premium and the 20th largest insurance company in Canada, by total assets.

Accident Fund: Accident Fund Insurance Company of America is an American workers' compensation insurance company headquartered in Lansing, Michigan.  The company is a member of AF Group, a premier provider of innovative insurance solutions.  Insurance policies may be issued by any of the following companies within AF Group: Accident Fund Insurance Company of America, Accident Fund National Insurance Company, Accident Fund General Insurance Company, United Wisconsin Insurance Company, Third Coast Insurance Company or CompWest Insurance Company.

Aviva: Aviva plc is a British multinational insurance company headquartered in London, United Kingdom.  It has about 33 million customers across 16 countries.  In the UK, Aviva is the largest general insurer and a leading life and pensions provider.  In addition, Aviva has a focus on five markets in Europe and in Asia, the company is focused on the growth markets of China and South East Asia.  Aviva is also the second largest general insurer in Canada.

Aviva Group Ireland: Aviva Group Ireland plc is the Irish arm of British insurance firm Aviva plc.  Its headquarters are in Dublin.  The company also provides investment management and pension services.  Hoover's reports that Aviva is the largest general insurer in Ireland, with a market share of more than 20%.  The company also has a majority shareholding in Aviva Health Insurance.

Princes House, Brighton: Princes House (formerly Norwich Union House) is an office and residential building in the centre of Brighton, part of the English coastal city of Brighton and Hove.  The prominently sited building, an example of Harry Stuart Goodhart-Rendel's "inimitable response to Modernism", was purpose-built as the headquarters of the Brighton & Sussex Building Society, forerunner of the Alliance & Leicester.  The office was later used by Norwich Union, another financial institution, and now houses a restaurant and flats.  The steel-framed structure is clad in red bricks with inlaid mosaicwork, forming a carefully detailed façade, and the corner elevation has an arrangement of brickwork and windows which suggests "the pleated folds of a curtain".  The building is listed it at Grade II for its architectural and historical importance.

NZI: NZI or New Zealand Insurance is a major insurance company in New Zealand.  NZI was formed in Auckland in 1859 as the New Zealand Insurance Company Ltd and is one of New Zealand's largest and longest-serving fire and general insurance brands.  It merged with South British Insurance in 1981; the two companies had been equally matched rivals and were virtually the same size, but with different emphasis on the types of business they held.  The new company formed a parent, New Zealand South British Group Ltd, which maintained both brands concurrently before changing to the NZI Corporation in 1984 when the South British brand was phased out.  In January 2003 IAG, Insurance Australia Group, purchased NZI when acquiring Aviva's general insurance business, and NZI is now a subsidiary of IAG New Zealand Ltd.  Aviva predecessor General Accident bought NZI in 1989.  NZI focuses on providing products to the intermediated market; i.e. brokers and banks.

Physicians Mutual: Physicians Mutual is a privately held insurance company headquartered in Omaha, Nebraska, United States, that consists of Physicians Mutual Insurance Company and Physicians Life Insurance Company.  Founded as Physicians Mutual Insurance Company in 1902 by Edwin E. Elliott, Physicians Mutual began by selling health insurance to medical professionals.  Policies were offered to the general public starting in 1962, and by 1970 the company expanded into life insurance when it founded Physicians Life Insurance Company.  Today the company offers a variety of insurance products, annuities, Medicare, Medigap, Medicare Supplement, Term Life Insurance, Whole Life Insurance, Cancer and funeral pre-planning services.  It holds over US$3 billion in assets and employs over one thousand people.  Robert A. Reed is chief executive officer and president.

Question: Princes House, Brighton had offices used by which British arm of Aviva insurance company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "building_name": {
      "type": "string",
      "description": "The name of the building in question."
    },
    "building_location": {
      "type": "string",
      "description": "The city where the building is located."
    },
    "former_building_name": {
      "type": "string",
      "description": "The previous name of the building."
    },
    "insurance_company_name": {
      "type": "string",
      "description": "The name of the insurance company that used offices in the building."
    },
    "company_relationship_to_aviva": {
      "type": "string",
      "description": "The relationship of the insurance company to Aviva."
    },
    "answer": {
      "type": "string",
      "description": "The final answer to the question."
    }
  },
  "required": [
    "building_name",
    "building_location",
    "former_building_name",
    "insurance_company_name",
    "company_relationship_to_aviva",
    "answer"
  ],
  "additionalProperties": false
}
