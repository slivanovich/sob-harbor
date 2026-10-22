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
Ecolab: Ecolab Inc., headquartered in St. Paul, Minnesota, is an American global provider of water, hygiene and energy technologies and services to the food, energy, healthcare, industrial and hospitality markets.  It was founded as Economics Laboratory in 1923 by Merritt J. Osborn, and renamed "Ecolab" in 1986.

Eddy Hartenstein: Eddy W. Hartenstein is an American media executive currently serving as a corporate director of Tribune Publishing and Yahoo!, he formerly served as President and CEO of the Tribune Company and publisher and CEO for the "Los Angeles Times".  He is a member of the Board of Directors of Broadcom Corporation, City of Hope National Medical Center, SanDisk, and Sirius XM Radio where he serves as lead independent director.

Jeffrey Ettinger: Jeffrey Ettinger (born 1959) is the former CEO of Hormel.  He assumed the role of President, CEO, and Chairman of the Board in 2005 and retired as CEO effective October 30, 2016.  He continues to serves as the company's Chairman of the Board.  He has been with the company since 1989, fulfilling roles such as senior corporate attorney, treasurer, and president of Jennie-O.  He is from Pasadena, California, and holds a business and law degree from UCLA.  He additionally serves as independent director Toro, Ecolab, North American Meat Institute, and Grocery Manufacturers Association.

Robert Milton: Robert A. Milton is the Chairman of the Board of Directors of United Continental Holdings which is the parent company of United Airlines.  He also serves as the Lead Independent Director of Air Lease Corporation.  He was the Chairman, President and Chief Executive Officer of ACE Aviation Holdings Inc., the parent company of Air Canada, from 2004 to 2017.  He is also a former Chairman, President and CEO of Air Canada.

Louis Hsieh: Louis Tung-jung Hsieh (, born 1965) is a Chinese businessman and lawyer and currently holds the position of Chief Financial Officer at NIO (or NextEV), a global startup based in China which designs and develops premium, smart electric vehicles and autonomous driving vehicles.  He also serves as a Senior Advisor and a Board Director of New Oriental Education and Technology Group (NYSE: EDU), China’s largest private educational services provider.  He was the company's president from May 2009 to January 2016.  He is also the Independent Director and Audit Chairman for each of JD.com, Inc. (NASDAQ: JD), China's largest direct sales Internet company, YUM China Holdings (NYSE: YUMC), the restaurant owner in China operating KFC, Pizza Hut, Little Sheep Hot Pot and Taco Bell, and Nord Anglia Education, Inc. (NYSE: NORD), a global schools organization.  He is also a board member at United Information Technologies, a Chinese storage solutions company.

Jacques van den Broek: Jacques van den Broek (born 24 May 1960, Goes) is the CEO of Randstad Holding since March 2014.  He also serves as the company's chairman.  He joined the company as a branch manager in 1988.  He once served as an independent director of Vedior.  He holds a degree in law from Tilburg University.

Bobby Mehta: Siddharth N. "Bobby" Mehta was former CEO and vice chairman of HSBC North America.  Mehta served as an Advisor of TransUnion since December 31, 2012.  Mehta serves as consultant of TransUnion.  He served the chief executive officer and president of TransUnion from August 2007 to December 31, 2012, and Transunion Financing Corp. until December 31, 2012.  From May 2007 to July 2007, he served as a consultant to the board of directors at TransUnion.  He served as the chief executive officer and president of TransUnion until December 31, 2012.  He served as the chief executive officer of TransUnion LLC.  He served as chairman of the board and chief executive officer of HSBC Finance Corporation from April 2005 to February 2007.  He served as chief executive officer and president of TransUnion LLC from 2007 to 2012.  From 1998 to 2007, he held a variety of positions with HSBC Finance Corporation and HSBC North America Holdings, Inc.  Mehta served as chief executive officer of HSBC North America until February 2007.  Mehta served as consultant of TransUnion since May 2007 until July 2007.  Mehta served as group managing director of HSBC Holdings PLC of HSBC Finance Corp. since April 30, 2005, and its unit chief executive officer since March 2005.  He served as the chief executive of HS BC North America Holdings Inc., of HSBC Finance Corp., from March 2005 to February 15, 2007.  He served as an executive chairman of HSBC Financial Corporation Limited since April 2005 and served as its chief executive officer from April 2005 to February 15, 2007.  He served as the chief executive officer of HSBC Bank USA, N.A. until February 2007.  He served as the chief executive officer of HSBC North America Holdings Inc. since March 2005.  He served as chairman and chief executive officer of HSBC Financial Corp., Ltd.  He oversaw HSBC's global credit card services, its North American consumer lending and mortgage services businesses and its first mortgage operation.  He was also responsible for corporate marketing, strategic planning and corporate development for HSBC North America Holdings Inc. and had responsibility for the strategic management of credit cards throughout the HSBC Group.  Mehta served as group executive of Credit Card Services, Auto Finance and Canada of Household International Inc., since July 2002.  He worked at MasterCard’s U.S. region board since March 2000.  Mehta joined Household International Inc., in 1998.  He served as senior vice president of The Boston Consulting Group in Los Angeles and co-leader of Boston Consulting Group Financial Services Practice in the United States.  Mehta served as a director of Global Board of MasterCard Incorporated since March 17, 2005.  He served as unit chairman of HSBC Holdings PLC and served as its board member since March 2005.  He served as vice chairman and director of HSBC Financial Corporation Limited., (Formerly Household International Inc.).  He has been a director of Avant Credit Corporation since December 18, 2014.  He has been an independent director of The Allstate Corporation since February 19, 2014.  He serves as a member of the advisory board at Core2 Group, Inc.  He has been non-executive independent director at Piramal Enterprises Ltd since April 1, 2013.  He serves on the boards of Datacard, Chicago Public Education Fund, University of Chicago Laboratory Schools, The Economic Club of Chicago, The Field Museum and Myelin Repair Foundation.  He serves as a director of TransUnion Corp. and TransUnion LLC.  He served as a director of MasterCard International Inc. (also known as MasterCard Worldwide) (formerly, MasterCard Inc.), since March 17, 2005.  He served as a director of HSBC Financial Corp.  Ltd.  He has been a director of TransUnion since April 2012.  Mehta serves on the board of international advisors for the Monterey, California, Institute of International Studies and is a member of the Financial Services Roundtable.  He also serves on the board of advisors for the Myelin Repair Foundation.  Mehta holds a Bachelor of Arts in economics from the London School of Economics and Masters of Business Administration from the University of Chicago.  He stepped down as head of the North American unit after the lender raised its forecast for bad loans in the U.S.  He is of Indian descent.

Patricia Russo: Patricia F. Russo (born June 12, 1952, in Trenton, New Jersey is an American businessperson.  Russo is most widely known for having served as Chief Executive Officer (CEO) of Lucent Technologies, and its successor, Alcatel-Lucent, a large communications equipment manufacturer.  She currently serves on the Board of Directors of General Motors, Merck & Co., and Arconic, Inc.  She serves as Chairwoman of the nonprofit organization, Partnership at Drugfree.org.  Prior to the split of Hewlett-Packard into two companies in 2015, Russo served as Lead Independent Director.  She now serves as Chairwoman of Hewlett Packard Enterprise.

Paul S. Atkins: Paul S. Atkins is CEO of Patomak Global Partners LLC, which provides consulting services regarding financial services industry matters, including regulatory compliance, risk and crisis management, public affairs, independent reviews, litigation support, and strategy.  He also serves as an independent director and non-executive chairman of the board of BATS Global Markets, Inc., a leading operator of electronic U.S. and European securities markets trading listed cash equity securities and equity options.

Independent director: An independent director (also sometimes known as an outside director) is a director (member) of a board of directors who does not have a material or pecuniary relationship with company or related persons, except sitting fees.  In the US, independent outsiders make up 66% of all boards and 72% of S&P 500 company boards, according to The Wall Street Journal.

Question: Jeffrey Ettinger serves as independent director for which company founded in 1923?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "role": {
      "type": "string",
      "description": "The role the person serves for the company."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the company that matches the criteria."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the company was founded."
    }
  },
  "required": [
    "person_name",
    "role",
    "company_name",
    "founding_year"
  ],
  "additionalProperties": false
}
