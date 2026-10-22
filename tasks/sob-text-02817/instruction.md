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
America's Freedom Festival at Provo: America's Freedom Festival at Provo (also America's Freedom Festival or Freedom Festival) is a private, non-profit, non-political foundation known for organizing more than 25 annual patriotic events in and around Provo, Utah.  It is one of the largest and longest (usually May - July) patriotic celebrations in the nation.  The organization's stated mission is to "celebrate, teach, honor, and strengthen the traditional American values of family, freedom, God, and country."  America's Freedom Festival sponsors one of the nation's largest Fourth of July celebrations, Stadium of Fire, held each year at LaVell Edwards Stadium on the campus of Brigham Young University.  Recent performers at Stadium of Fire include Journey (band), Cirque du Soleil, Carrie Underwood, Brad Paisley, and the Blue Man Group.  The United States Department of Defense has chosen to broadcast parts of the festival to millions of servicemen and women serving abroad in the Armed Forces for the past several years.

Windsor–Detroit International Freedom Festival: The International Freedom Festival is a multi-day celebration in late June marking Canada Day on July 1 and the American Independence Day on July 4.  Detroit, Michigan, in the United States and Windsor, Ontario, in Canada jointly celebrate the multi-day festival which draws about 3.5 million visitors.  The International Freedom Festival began in 1959.

The Scandal of the Evangelical Mind: The Scandal of the Evangelical Mind (published 1994) is a book by evangelical Christian scholar Mark A. Noll, who is currently Francis A. McAnaney Professor of History at the University of Notre Dame.  As a critique of the waning influence of intellectual pursuits within the American evangelical community, the book is both a scholarly analysis of evangelical anti-intellectualism and "an epistle from a wounded lover" by an intellectual who feels betrayed by evangelical Christianity's neglect of "sober analysis of nature, human society, and the arts".  "Scandal" was named "Book of the Year" by "Christianity Today", the popular neo-evangelical Christian magazine.  In 2004, ten years after its initial publication, "Christianity Today" claimed that the book had "arguably shaped the evangelical world (or at least its institutions) more than any other book published in the last decade".

Freedom Festival, Hull: The Freedom Festival is an annual music and performance arts festival held in the city of Kingston upon Hull, East Riding of Yorkshire, England.  It is named in honour of the slave trade abolitionist, MP and son of Hull, William Wilberforce.  The festival was established in 2007 to mark the 200th anniversary of Wilberforce's law, the Slave Trade Act 1807, to abolish the slave trade in the British Empire.

World Evangelical Alliance: The World Evangelical Alliance (WEA) is a global organization of evangelical Christian churches, serving more than 600 million evangelicals, founded in 1846 in London, England to unite evangelicals worldwide.  WEA is the largest international organization of evangelical churches, and is now headquartered in New York City, United States.  It brings together 7 regional and 129 evangelical alliances of churches, and over 150 member organizations.  Some of the national alliances include Protestant churches which are not traditional Evangelical churches in the strict sense (anabaptism), (Networks & Church Denominations).  Moreover, the WEA includes a certain percentage of individual evangelical Christian churches.  It is open for membership of individual evangelical Christians (as compared to the World Council of Churches (WCC), where individual membership is not possible).  The Evangelical Alliance of Great Britain, its founding member, is part of WEA.

Stadium of Fire: The Stadium of Fire is an annual event held in the Brigham Young University's LaVell Edwards Stadium on or very near the United States' Independence Day.  It is one of the main events for the America's Freedom Festival.  This patriotic extravaganza with a cast of thousands features the largest stadium fireworks show in America.  It is also televised worldwide to America's troops and their families on American Forces TV, as a gift from America's Freedom Festival.

Dalit Freedom Network: Dalit Freedom Network is an evangelical Christian organization whose claimed official mission is to "empower the Dalits in their quest for social freedom and human dignity by networking human, financial, and informational resources."  Founded by Dr. Joseph D'souza, who heads the All India Christian Council, and Nanci Ricks, DFN is located in Colorado.  The Dalit Freedom Network is a partner of the All India Christian Council, a nationwide alliance of more than 2000 Christian denominations, mission agencies, institutions, federations in India. As per Dr. Joseph D'Souza's biography on The 700 Club's website : "The Dalit Freedom Network grew out of the AICC's (All India Christian Council's) need to facilitate work in the United States".

Evangelical Christian Church in Canada: The Evangelical Christian Church (Christian Disciples) as an evangelical Protestant Canadian church body in North America (2004) can be traced to the formal organization of the Christian Church (Disciples of Christ) in 1804, in Bourbon County, Kentucky under the leadership of Barton Warren Stone (1772–1844).  The Stone Movement later merged with the efforts of Thomas Campbell (1772–1854) and his son Alexander Campbell (1788–1866) to become the Restoration Movement that gave birth to the Churches of Christ (Non-Instrumental), the Christian churches and churches of Christ, the Churches of Christ (non-institutional), and the Disciples of Christ.  The Evangelical Christian Church (Christian Disciples) as a separate group within the Restoration tradition was reorganized in 2001.  The Evangelical Christian Church's national office in Canada is in Waterloo, Ontario.

Brazilian Evangelical Christian Alliance: The Brazilian Evangelical Christian Alliance is a national evangelical alliance, member of the World Evangelical Alliance.  It regroup Evangelical Christian denominations, organizations, educational institutions and local churches in Brazil.  The headquarters is in Campinas, Brazil.  Its President is Silas Tostes.

William Wilberforce: William Wilberforce (24 August 175929 July 1833) was an English politician, philanthropist, and a leader of the movement to stop the slave trade.  A native of Kingston upon Hull, Yorkshire, he began his political career in 1780, eventually becoming an independent Member of Parliament (MP) for Yorkshire (1784–1812).  In 1785, he became an Evangelical Christian, which resulted in major changes to his lifestyle and a lifelong concern for reform.

Question: What year did the man that the Freedom Festival is named after become an Evangelical Christian?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person the festival is named after."
    },
    "event_description": {
      "type": "string",
      "description": "Description of the significant event in the person's life."
    },
    "year_of_event": {
      "type": "integer",
      "description": "The year the described event occurred."
    },
    "festival_named_after_person": {
      "type": "string",
      "description": "The name of the festival that is named in honor of this person."
    }
  },
  "required": [
    "person_name",
    "event_description",
    "year_of_event",
    "festival_named_after_person"
  ],
  "additionalProperties": false
}
