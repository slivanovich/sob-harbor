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
Lide Meriwether: Lide Smith Meriwether (October 16, 1829 – September 28, 1913) was a leader of the first generation of feminists and women's rights activists.  She lobbied for prohibition, raising the legal age of consent, and woman's suffrage.  Meriwether was president of the Tennessee Woman's Christian Temperance Union (WCTU) from 1884 to 1897, and then as an honorary president for life.  In 1889, she organized the first Equal Rights Association in Memphis, and served as president of the Tennessee Equal Rights Association from 1897 to 1900, and subsequently was made honorary president for life.

Flint House, Buckinghamshire: Flint House is a house near Waddesdon Manor, Buckinghamshire, England.  It was commissioned by Jacob Rothschild, 4th Baron Rothschild and completed in 2015.  It is on the Waddesdon Manor estate.  The architect was Charlotte Skene Catling, with interiors by David Mlinaric.  The building is designed in an unusual triangular shape.  It is open to visitors at certain times or for group visits.

World Association of Chefs' Societies: The World Association of Chefs' Societies (WACS), is a global network of chefs associations first founded in October 1928 at the Sorbonne in Paris.  At that first congress there were 65 delegates from 17 countries, representing 36 national and international associations, and the venerable August Escoffier was named the first Honorary President of WACS.  Today, this global body has over 100 official chefs associations as members.  The biennial congress is a hallmark tradition of WACS and has been organized in over 20 cities across the world throughout its illustrious 89-year history, WACS is managed by an elected presidential body consisting of the WACS president, vice president, treasurer, secretary general and ambassador honorary president, as well as a board of continental directors that look after the regions of Asia, Europe, Africa, the Pacific and the Americas.  A separate committee manages all culinary competition-related affairs.

Derick Thomson: Derick Smith Thomson (5 August 1921 – 21 March 2012), known as "Ruaraidh MacThòmais" in his native Gaelic, was a Scottish poet, publisher, lexicographer, academic and writer.  He was originally from Lewis, but spent much of his life in Glasgow, where he was Professor of Celtic at the University of Glasgow from 1963 to 1991.  He is best known for setting up the publishing house Gairm, along with its magazine, which was the longest-running periodical ever to be written entirely in Gaelic, running for over fifty years under his editorship.  Gairm has since ceased, and was replaced by "Gath" and then STEALL.  He was an Honorary President of the Scottish Poetry Library, and a Fellow of the Royal Society of Edinburgh and the British Academy.  In June 2007, he received an honorary degree from Glasgow University.

Lam Chiu Ying: Lam Chiu-ying (), , also known by the nickname 'Black Ying' (), is a Hong Kong meteorologist, bird-watcher, conservationist and blogger.  He was the director of the Hong Kong observatory 2003 through 2009.  He is also an honorary fellow of the Royal Meteorological Society, an Honorary University Fellow of the University of Hong Kong as well as the honorary president of the Hong Kong Bird Watching Society.  Microplanet 64288 Lamchiuying is named after Lam.

Flint House (Massachusetts): The Flint House is a historic First Period house at 28 Lexington Road in Lincoln, Massachusetts.  The oldest portions of this house have very early colonial construction, and its main block either is, or contains portions of, a "mansion" built by Ephraim Flint and mentioned in a 1709 deed.  This main block appears to have portions of two older structures that were joined together; the exact sequence of construction is difficult due to extensive alterations of the building over the 18th and 19th centuries.  The property includes a barn which is thought to have been built before 1750, and is remarkably unaltered despite having been moved a relatively short distance on the grounds.  The house has been occupied by nine generations of Flints, who have been a major force in the civic life of Lincoln.

Mosibudi Mangena: Mosibudi Mangena (born 7 August 1947 in Tzaneen, Transvaal) is a South Africa politician, former President of the Azanian People's Organisation (AZAPO).  He is also currently the honorary President of AZAPO while Jacob Dikobo is the current President, this is not unusual in the Black Consciousness Movement as was the case with Steve Biko who was also the honorary President of the Black People's Convention in the early-1970s while Winfrey Kgware was the President.  He was the Minister of Science and Technology (29 April 2004 - 10 May 2009).

V. N. Rajasekharan Pillai: Prof. V. N. Rajasekharan Pillai (; born 20 October 1949) is President of Mewar University, Chiittorgarh, Rajasthan, India.  Concurrently he serves as the Honorary President of the Human Development Foundation India, a Civil Society Organisation in the National Capital Region, New Delhi.  He was Executive Vice-President of the Kerala State Council for Science, Technology and Environment, Govt of Kerala during the period 2011-2014.  Simultaneously he held positions as the Principal Secretary, Science & Technology Dept of the Govt of Kerala, Chairman of the Kerala Coastal Zone Management Authority and the Kerala Biotechnology Commission.  Prior to that Prof. Pillai was the Vice-Chancellor of the Indira Gandhi National Open University ( IGNOU ), New Delhi ( 2006-2011) holding simultaneously the position of the Chairman, Distance Education Council, Govt of India.  He served as Vice-Chairman & Chairman of the University Grants Commission, Govt of India, New Delhi during the period 2003-2006.  He was the Executive Director of the National Assessment and Accreditaition Council ( NAAC), Govt of India, during the period 2000-2003.  Prior to that Prof. V. N. Rajasekharan Pillai was the Vice-Chancellor of the Mahatma Gandhi University, Kottayam, Govt of Kerala and held additional charge of the Cochin University of Science and Technology (1996-2000).  In 2000 he was on a Visiting Research Professor assignment in the University of Lausanne, Switzerland.  From 1983 to 1986, Dr. Pillai worked in various academic and research executive positions in the Mahatma Gandhi University, Kottayam such as the Founder Professor and Director of the School of Chemical Sciences, Dean of Faculty of Science, Founder Director of the School of Professional Distance Education, Director, College Development Council and Controller of Examinations of the University.  During the period 1977-1983, Dr. Pillai worked as a Post-Doctoral Research Fellow, on deputation from Calicut University, Kerala, in the Universities of Tubigen and Mainz, Germany.  From 1971 to 1983, he worked in the Universities of Kerala and Calicut University as UGC/CSIR Junor and Senior Research Fellow, Assistant Professor and Associate Professor in the area of Chemical Sciences.  Professor Rajasekharan Pillai is an Elected Fellow of the Indian Academy of Sciences.  Distinguished Fellow of the Kerala Academy of Sciences, and an Honorary Fellow of the Institution of Electronics and Telecommunication Engineers ( IETE), New Delhi.  He was also a Fellow of the Royal Society of Chemistry and an Honorary Senior Fellow of the Jawaharlal Nehru Centre for Advanced Scientific Research, Banaglaore.

Jacob Rothschild, 4th Baron Rothschild: Nathaniel Charles Jacob Rothschild, 4th Baron Rothschild, {'1': ", '2': ", '3': ", '4': "} (born 29 April 1936) is a British investment banker and a member of the prominent Rothschild banking family.  He is also Honorary President of the Institute for Jewish Policy Research.

Police Rehabilitation Centre, Flint House: The house and surrounding 14 acre estate were purchased by the Police Convalescent Home Management Committee on 20 April 1985 after the previous centre, Kingsway, was deemed to be too small.  After renovation works, Flint House was opened as a Police Rehabilitation Centre by Queen Elizabeth the Queen Mother on 2 June 1988.  The house had previously been a training centre for the Water Industry Training Board, and later Thames Water, complete with a complex system of pipes for trainees to detect leaks.

Question: The man that commissioned the Flint House is Honorary President of what institue?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "commissioner_name": {
      "type": "string",
      "description": "The name of the person who commissioned the Flint House."
    },
    "house_name": {
      "type": "string",
      "description": "The name of the house that was commissioned."
    },
    "honorary_president_of": {
      "type": "string",
      "description": "The name of the institute or organization for which the commissioner serves as Honorary President."
    }
  },
  "required": [
    "commissioner_name",
    "house_name",
    "honorary_president_of"
  ],
  "additionalProperties": false
}
