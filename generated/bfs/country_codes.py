"""Auto-generated from BFS data.

DO NOT EDIT MANUALLY!

Generated: 2025-10-27T15:50:57.921965
Source: be-b-00.04-sg-01.xlsx
Description: BFS Official Country and Territory Codes (Staaten- und Gebietsverzeichnis)

DATA SOURCE ATTRIBUTION:
    Data Provider: Swiss Federal Statistical Office (BFS)
    Dataset: Country and Territory Codes (Staaten- und Gebietsverzeichnis)
    Terms of Use: Open Government Data (OGD) Switzerland - "Open use. Must provide the source."
    URL: https://www.bfs.admin.ch/
    Copyright: © 2024 Swiss Federal Statistical Office (BFS)

    This data is made available under Swiss OGD terms, which require source attribution.
    See DATA_SOURCES.md in the repository root for complete licensing information.

CODE LICENSE:
    This Python code structure is © 2025 OpenMun Project, licensed under MIT License.
    The data content is © Swiss Federal Statistical Office (BFS), used under OGD terms.

Run importers/bfs_country_importer.py to regenerate.
"""

# ISO 3166-1 alpha-2 codes mapped to BFS codes and names
COUNTRY_CODES = {
    'AD': {
        'bfs_code': '8202',
        'iso3': 'AND',
        'names': {
            'de': 'Andorra',
            'fr': 'Andorre',
            'it': 'Andorra',
            'en': 'Andorra',
        }
    },
    'AE': {
        'bfs_code': '8532',
        'iso3': 'ARE',
        'names': {
            'de': 'Vereinigte Arabische Emirate',
            'fr': 'Emirats arabes unis',
            'it': 'Emirati arabi uniti',
            'en': 'United Arab Emirates',
        }
    },
    'AF': {
        'bfs_code': '8501',
        'iso3': 'AFG',
        'names': {
            'de': 'Afghanistan',
            'fr': 'Afghanistan',
            'it': 'Afghanistan',
            'en': 'Afghanistan',
        }
    },
    'AG': {
        'bfs_code': '8442',
        'iso3': 'ATG',
        'names': {
            'de': 'Antigua und Barbuda',
            'fr': 'Antigua-et-Barbuda',
            'it': 'Antigua e Barbuda',
            'en': 'Antigua and Barbuda',
        }
    },
    'AI': {
        'bfs_code': '8446',
        'iso3': 'AIA',
        'names': {
            'de': 'Anguilla',
            'fr': 'Anguilla',
            'it': 'Anguilla',
            'en': 'Anguilla',
        }
    },
    'AL': {
        'bfs_code': '8201',
        'iso3': 'ALB',
        'names': {
            'de': 'Albanien',
            'fr': 'Albanie',
            'it': 'Albania',
            'en': 'Albania',
        }
    },
    'AM': {
        'bfs_code': '8560',
        'iso3': 'ARM',
        'names': {
            'de': 'Armenien',
            'fr': 'Arménie',
            'it': 'Armenia',
            'en': 'Armenia',
        }
    },
    'AO': {
        'bfs_code': '8305',
        'iso3': 'AGO',
        'names': {
            'de': 'Angola',
            'fr': 'Angola',
            'it': 'Angola',
            'en': 'Angola',
        }
    },
    'AQ': {
        'bfs_code': '8701',
        'iso3': 'ATA',
        'names': {
            'de': 'Antarktis',
            'fr': 'Antarctique',
            'it': 'Antartide',
            'en': 'Antarctica',
        }
    },
    'AR': {
        'bfs_code': '8401',
        'iso3': 'ARG',
        'names': {
            'de': 'Argentinien',
            'fr': 'Argentine',
            'it': 'Argentina',
            'en': 'Argentina',
        }
    },
    'AS': {
        'bfs_code': '8621',
        'iso3': 'ASM',
        'names': {
            'de': 'Amerikanisch-Samoa',
            'fr': 'Samoa américaines',
            'it': 'Samoa americane',
            'en': 'American Samoa',
        }
    },
    'AT': {
        'bfs_code': '8229',
        'iso3': 'AUT',
        'names': {
            'de': 'Österreich',
            'fr': 'Autriche',
            'it': 'Austria',
            'en': 'Austria',
        }
    },
    'AU': {
        'bfs_code': '8601',
        'iso3': 'AUS',
        'names': {
            'de': 'Australien',
            'fr': 'Australie',
            'it': 'Australia',
            'en': 'Australia',
        }
    },
    'AW': {
        'bfs_code': '8482',
        'iso3': 'ABW',
        'names': {
            'de': 'Aruba',
            'fr': 'Aruba',
            'it': 'Aruba',
            'en': 'Aruba',
        }
    },
    'AX': {
        'bfs_code': '8274',
        'iso3': 'ALA',
        'names': {
            'de': 'Alandinseln',
            'fr': 'Îles d\'Aland',
            'it': 'Isole di Aland',
            'en': 'Aland Islands',
        }
    },
    'AZ': {
        'bfs_code': '8561',
        'iso3': 'AZE',
        'names': {
            'de': 'Aserbaidschan',
            'fr': 'Azerbaïdjan',
            'it': 'Azerbaigian',
            'en': 'Azerbaijan',
        }
    },
    'BA': {
        'bfs_code': '8252',
        'iso3': 'BIH',
        'names': {
            'de': 'Bosnien und Herzegowina',
            'fr': 'Bosnie et Herzégovine',
            'it': 'Bosnia e Erzegovina',
            'en': 'Bosnia and Herzegovina',
        }
    },
    'BB': {
        'bfs_code': '8403',
        'iso3': 'BRB',
        'names': {
            'de': 'Barbados',
            'fr': 'Barbade',
            'it': 'Barbados',
            'en': 'Barbados',
        }
    },
    'BD': {
        'bfs_code': '8546',
        'iso3': 'BGD',
        'names': {
            'de': 'Bangladesch',
            'fr': 'Bangladesh',
            'it': 'Bangladesh',
            'en': 'Bangladesh',
        }
    },
    'BE': {
        'bfs_code': '8204',
        'iso3': 'BEL',
        'names': {
            'de': 'Belgien',
            'fr': 'Belgique',
            'it': 'Belgio',
            'en': 'Belgium',
        }
    },
    'BF': {
        'bfs_code': '8337',
        'iso3': 'BFA',
        'names': {
            'de': 'Burkina Faso',
            'fr': 'Burkina Faso',
            'it': 'Burkina Faso',
            'en': 'Burkina Faso',
        }
    },
    'BG': {
        'bfs_code': '8205',
        'iso3': 'BGR',
        'names': {
            'de': 'Bulgarien',
            'fr': 'Bulgarie',
            'it': 'Bulgaria',
            'en': 'Bulgaria',
        }
    },
    'BH': {
        'bfs_code': '8502',
        'iso3': 'BHR',
        'names': {
            'de': 'Bahrain',
            'fr': 'Bahreïn',
            'it': 'Bahrein',
            'en': 'Bahrain',
        }
    },
    'BI': {
        'bfs_code': '8308',
        'iso3': 'BDI',
        'names': {
            'de': 'Burundi',
            'fr': 'Burundi',
            'it': 'Burundi',
            'en': 'Burundi',
        }
    },
    'BJ': {
        'bfs_code': '8309',
        'iso3': 'BEN',
        'names': {
            'de': 'Benin',
            'fr': 'Bénin',
            'it': 'Benin',
            'en': 'Benin',
        }
    },
    'BL': {
        'bfs_code': '8449',
        'iso3': 'BLM',
        'names': {
            'de': 'Saint-Barthélemy',
            'fr': 'Saint-Barthélemy',
            'it': 'Saint-Barthélemy',
            'en': 'Saint Barthélemy',
        }
    },
    'BM': {
        'bfs_code': '8404',
        'iso3': 'BMU',
        'names': {
            'de': 'Bermuda',
            'fr': 'Bermudes',
            'it': 'Bermuda',
            'en': 'Bermuda',
        }
    },
    'BN': {
        'bfs_code': '8504',
        'iso3': 'BRN',
        'names': {
            'de': 'Brunei Darussalam',
            'fr': 'Brunéi Darussalam',
            'it': 'Brunei Darussalam',
            'en': 'Brunei',
        }
    },
    'BO': {
        'bfs_code': '8405',
        'iso3': 'BOL',
        'names': {
            'de': 'Bolivien',
            'fr': 'Bolivie',
            'it': 'Bolivia',
            'en': 'Bolivia',
        }
    },
    'BQ': {
        'bfs_code': '8486',
        'iso3': 'BES',
        'names': {
            'de': 'Bonaire, Saint Eustatius und Saba',
            'fr': 'Bonaire, Saint Eustatius et Saba',
            'it': 'Bonaire, Saint Eustatius e Saba',
            'en': 'Bonaire, Saint Eustatius and Saba',
        }
    },
    'BR': {
        'bfs_code': '8406',
        'iso3': 'BRA',
        'names': {
            'de': 'Brasilien',
            'fr': 'Brésil',
            'it': 'Brasile',
            'en': 'Brazil',
        }
    },
    'BS': {
        'bfs_code': '8402',
        'iso3': 'BHS',
        'names': {
            'de': 'Bahamas',
            'fr': 'Bahamas',
            'it': 'Bahamas',
            'en': 'Bahamas',
        }
    },
    'BT': {
        'bfs_code': '8503',
        'iso3': 'BTN',
        'names': {
            'de': 'Bhutan',
            'fr': 'Bhoutan',
            'it': 'Bhutan',
            'en': 'Bhutan',
        }
    },
    'BV': {
        'bfs_code': '8702',
        'iso3': 'BVT',
        'names': {
            'de': 'Bouvetinsel',
            'fr': 'Île Bouvet',
            'it': 'Isola Bouvet',
            'en': 'Bouvet Island',
        }
    },
    'BW': {
        'bfs_code': '8307',
        'iso3': 'BWA',
        'names': {
            'de': 'Botsuana',
            'fr': 'Botswana',
            'it': 'Botswana',
            'en': 'Botswana',
        }
    },
    'BY': {
        'bfs_code': '8266',
        'iso3': 'BLR',
        'names': {
            'de': 'Belarus',
            'fr': 'Bélarus',
            'it': 'Belarus',
            'en': 'Belarus',
        }
    },
    'BZ': {
        'bfs_code': '8419',
        'iso3': 'BLZ',
        'names': {
            'de': 'Belize',
            'fr': 'Belize',
            'it': 'Belize',
            'en': 'Belize',
        }
    },
    'CA': {
        'bfs_code': '8423',
        'iso3': 'CAN',
        'names': {
            'de': 'Kanada',
            'fr': 'Canada',
            'it': 'Canada',
            'en': 'Canada',
        }
    },
    'CC': {
        'bfs_code': '8652',
        'iso3': 'CCK',
        'names': {
            'de': 'Kokosinseln',
            'fr': 'Îles Cocos (Keeling)',
            'it': 'Isole Cocos',
            'en': 'Cocos (Keeling) Islands',
        }
    },
    'CD': {
        'bfs_code': '8323',
        'iso3': 'COD',
        'names': {
            'de': 'Kongo (Kinshasa)',
            'fr': 'Congo (Kinshasa)',
            'it': 'Congo (Kinshasa)',
            'en': 'Congo (Kinshasa)',
        }
    },
    'CF': {
        'bfs_code': '8360',
        'iso3': 'CAF',
        'names': {
            'de': 'Zentralafrikanische Republik',
            'fr': 'République centrafricaine',
            'it': 'Repubblica centrafricana',
            'en': 'Central African Republic',
        }
    },
    'CG': {
        'bfs_code': '8322',
        'iso3': 'COG',
        'names': {
            'de': 'Kongo (Brazzaville)',
            'fr': 'Congo (Brazzaville)',
            'it': 'Congo (Brazzaville)',
            'en': 'Congo (Brazzaville)',
        }
    },
    'CH': {
        'bfs_code': '8100',
        'iso3': 'CHE',
        'names': {
            'de': 'Schweiz',
            'fr': 'Suisse',
            'it': 'Svizzera',
            'en': 'Switzerland',
        }
    },
    'CI': {
        'bfs_code': '8310',
        'iso3': 'CIV',
        'names': {
            'de': 'Côte d\'Ivoire',
            'fr': 'Côte d\'Ivoire',
            'it': 'Côte d\'Ivoire',
            'en': 'Côte d\'Ivoire',
        }
    },
    'CK': {
        'bfs_code': '8682',
        'iso3': 'COK',
        'names': {
            'de': 'Cookinseln',
            'fr': 'Îles Cook',
            'it': 'Isole Cook',
            'en': 'Cook Islands',
        }
    },
    'CL': {
        'bfs_code': '8407',
        'iso3': 'CHL',
        'names': {
            'de': 'Chile',
            'fr': 'Chili',
            'it': 'Cile',
            'en': 'Chile',
        }
    },
    'CM': {
        'bfs_code': '8317',
        'iso3': 'CMR',
        'names': {
            'de': 'Kamerun',
            'fr': 'Cameroun',
            'it': 'Camerun',
            'en': 'Cameroon',
        }
    },
    'CN': {
        'bfs_code': '8508',
        'iso3': 'CHN',
        'names': {
            'de': 'China',
            'fr': 'Chine',
            'it': 'Cina',
            'en': 'China',
        }
    },
    'CO': {
        'bfs_code': '8424',
        'iso3': 'COL',
        'names': {
            'de': 'Kolumbien',
            'fr': 'Colombie',
            'it': 'Colombia',
            'en': 'Colombia',
        }
    },
    'CR': {
        'bfs_code': '8408',
        'iso3': 'CRI',
        'names': {
            'de': 'Costa Rica',
            'fr': 'Costa Rica',
            'it': 'Costa Rica',
            'en': 'Costa Rica',
        }
    },
    'CU': {
        'bfs_code': '8425',
        'iso3': 'CUB',
        'names': {
            'de': 'Kuba',
            'fr': 'Cuba',
            'it': 'Cuba',
            'en': 'Cuba',
        }
    },
    'CV': {
        'bfs_code': '8319',
        'iso3': 'CPV',
        'names': {
            'de': 'Cabo Verde',
            'fr': 'Cabo Verde',
            'it': 'Cabo Verde',
            'en': 'Cabo Verde',
        }
    },
    'CW': {
        'bfs_code': '8484',
        'iso3': 'CUW',
        'names': {
            'de': 'Curaçao',
            'fr': 'Curaçao',
            'it': 'Curaçao',
            'en': 'Curaçao',
        }
    },
    'CX': {
        'bfs_code': '8655',
        'iso3': 'CXR',
        'names': {
            'de': 'Weihnachtsinsel',
            'fr': 'Île Christmas (Australie)',
            'it': 'Isola Christmas',
            'en': 'Christmas Island',
        }
    },
    'CY': {
        'bfs_code': '8242',
        'iso3': 'CYP',
        'names': {
            'de': 'Zypern',
            'fr': 'Chypre',
            'it': 'Cipro',
            'en': 'Cyprus',
        }
    },
    'CZ': {
        'bfs_code': '8244',
        'iso3': 'CZE',
        'names': {
            'de': 'Tschechien',
            'fr': 'Tchéquie',
            'it': 'Cechia',
            'en': 'Czechia',
        }
    },
    'DE': {
        'bfs_code': '8207',
        'iso3': 'DEU',
        'names': {
            'de': 'Deutschland',
            'fr': 'Allemagne',
            'it': 'Germania',
            'en': 'Germany',
        }
    },
    'DJ': {
        'bfs_code': '8303',
        'iso3': 'DJI',
        'names': {
            'de': 'Dschibuti',
            'fr': 'Djibouti',
            'it': 'Gibuti',
            'en': 'Djibouti',
        }
    },
    'DK': {
        'bfs_code': '8206',
        'iso3': 'DNK',
        'names': {
            'de': 'Dänemark',
            'fr': 'Danemark',
            'it': 'Danimarca',
            'en': 'Denmark',
        }
    },
    'DM': {
        'bfs_code': '8440',
        'iso3': 'DMA',
        'names': {
            'de': 'Dominica',
            'fr': 'Dominique',
            'it': 'Dominica',
            'en': 'Dominica',
        }
    },
    'DO': {
        'bfs_code': '8409',
        'iso3': 'DOM',
        'names': {
            'de': 'Dominikanische Republik',
            'fr': 'République dominicaine',
            'it': 'Repubblica dominicana',
            'en': 'Dominican Republic',
        }
    },
    'DZ': {
        'bfs_code': '8304',
        'iso3': 'DZA',
        'names': {
            'de': 'Algerien',
            'fr': 'Algérie',
            'it': 'Algeria',
            'en': 'Algeria',
        }
    },
    'EC': {
        'bfs_code': '8410',
        'iso3': 'ECU',
        'names': {
            'de': 'Ecuador',
            'fr': 'Équateur',
            'it': 'Ecuador',
            'en': 'Ecuador',
        }
    },
    'EE': {
        'bfs_code': '8260',
        'iso3': 'EST',
        'names': {
            'de': 'Estland',
            'fr': 'Estonie',
            'it': 'Estonia',
            'en': 'Estonia',
        }
    },
    'EG': {
        'bfs_code': '8359',
        'iso3': 'EGY',
        'names': {
            'de': 'Ägypten',
            'fr': 'Égypte',
            'it': 'Egitto',
            'en': 'Egypt',
        }
    },
    'EH': {
        'bfs_code': '8372',
        'iso3': 'ESH',
        'names': {
            'de': 'Westsahara',
            'fr': 'Sahara Occidental',
            'it': 'Sahara Occidentale',
            'en': 'Western Sahara',
        }
    },
    'ER': {
        'bfs_code': '8362',
        'iso3': 'ERI',
        'names': {
            'de': 'Eritrea',
            'fr': 'Érythrée',
            'it': 'Eritrea',
            'en': 'Eritrea',
        }
    },
    'ES': {
        'bfs_code': '8236',
        'iso3': 'ESP',
        'names': {
            'de': 'Spanien',
            'fr': 'Espagne',
            'it': 'Spagna',
            'en': 'Spain',
        }
    },
    'ET': {
        'bfs_code': '8302',
        'iso3': 'ETH',
        'names': {
            'de': 'Äthiopien',
            'fr': 'Éthiopie',
            'it': 'Etiopia',
            'en': 'Ethiopia',
        }
    },
    'FI': {
        'bfs_code': '8211',
        'iso3': 'FIN',
        'names': {
            'de': 'Finnland',
            'fr': 'Finlande',
            'it': 'Finlandia',
            'en': 'Finland',
        }
    },
    'FJ': {
        'bfs_code': '8602',
        'iso3': 'FJI',
        'names': {
            'de': 'Fidschi',
            'fr': 'Fidji',
            'it': 'Figi',
            'en': 'Fiji',
        }
    },
    'FK': {
        'bfs_code': '8412',
        'iso3': 'FLK',
        'names': {
            'de': 'Falklandinseln',
            'fr': 'Îles Falkland',
            'it': 'Isole Falkland',
            'en': 'Falkland Islands',
        }
    },
    'FM': {
        'bfs_code': '8618',
        'iso3': 'FSM',
        'names': {
            'de': 'Mikronesien',
            'fr': 'Micronésie',
            'it': 'Micronesia',
            'en': 'Micronesia',
        }
    },
    'FO': {
        'bfs_code': '8210',
        'iso3': 'FRO',
        'names': {
            'de': 'Färöer',
            'fr': 'Îles Féroé',
            'it': 'Isole Faer Oer',
            'en': 'Faeroe Islands',
        }
    },
    'FR': {
        'bfs_code': '8212',
        'iso3': 'FRA',
        'names': {
            'de': 'Frankreich',
            'fr': 'France',
            'it': 'Francia',
            'en': 'France',
        }
    },
    'GA': {
        'bfs_code': '8311',
        'iso3': 'GAB',
        'names': {
            'de': 'Gabun',
            'fr': 'Gabon',
            'it': 'Gabon',
            'en': 'Gabon',
        }
    },
    'GB': {
        'bfs_code': '8215',
        'iso3': 'GBR',
        'names': {
            'de': 'Vereinigtes Königreich',
            'fr': 'Royaume-Uni',
            'it': 'Regno Unito',
            'en': 'United Kingdom',
        }
    },
    'GD': {
        'bfs_code': '8441',
        'iso3': 'GRD',
        'names': {
            'de': 'Grenada',
            'fr': 'Grenade',
            'it': 'Grenada',
            'en': 'Grenada',
        }
    },
    'GE': {
        'bfs_code': '8562',
        'iso3': 'GEO',
        'names': {
            'de': 'Georgien',
            'fr': 'Géorgie',
            'it': 'Georgia',
            'en': 'Georgia',
        }
    },
    'GF': {
        'bfs_code': '8416',
        'iso3': 'GUF',
        'names': {
            'de': 'Französisch-Guayana',
            'fr': 'Guyane Française',
            'it': 'Guiana Francese',
            'en': 'French Guyana',
        }
    },
    'GG': {
        'bfs_code': '8272',
        'iso3': 'GGY',
        'names': {
            'de': 'Guernsey',
            'fr': 'Guernesey',
            'it': 'Guernsey',
            'en': 'Guernsey',
        }
    },
    'GH': {
        'bfs_code': '8313',
        'iso3': 'GHA',
        'names': {
            'de': 'Ghana',
            'fr': 'Ghana',
            'it': 'Ghana',
            'en': 'Ghana',
        }
    },
    'GI': {
        'bfs_code': '8213',
        'iso3': 'GIB',
        'names': {
            'de': 'Gibraltar',
            'fr': 'Gibraltar',
            'it': 'Gibilterra',
            'en': 'Gibraltar',
        }
    },
    'GL': {
        'bfs_code': '8413',
        'iso3': 'GRL',
        'names': {
            'de': 'Grönland',
            'fr': 'Groenland',
            'it': 'Groenlandia',
            'en': 'Greenland',
        }
    },
    'GM': {
        'bfs_code': '8312',
        'iso3': 'GMB',
        'names': {
            'de': 'Gambia',
            'fr': 'Gambie',
            'it': 'Gambia',
            'en': 'Gambia',
        }
    },
    'GN': {
        'bfs_code': '8315',
        'iso3': 'GIN',
        'names': {
            'de': 'Guinea',
            'fr': 'Guinée',
            'it': 'Guinea',
            'en': 'Guinea',
        }
    },
    'GP': {
        'bfs_code': '8414',
        'iso3': 'GLP',
        'names': {
            'de': 'Guadeloupe',
            'fr': 'Guadeloupe',
            'it': 'Guadalupa',
            'en': 'Guadeloupe',
        }
    },
    'GQ': {
        'bfs_code': '8301',
        'iso3': 'GNQ',
        'names': {
            'de': 'Äquatorialguinea',
            'fr': 'Guinée équatoriale',
            'it': 'Guinea equatoriale',
            'en': 'Equatorial Guinea',
        }
    },
    'GR': {
        'bfs_code': '8214',
        'iso3': 'GRC',
        'names': {
            'de': 'Griechenland',
            'fr': 'Grèce',
            'it': 'Grecia',
            'en': 'Greece',
        }
    },
    'GS': {
        'bfs_code': '8483',
        'iso3': 'SGS',
        'names': {
            'de': 'Südgeorgien und Südliche Sandwichinseln',
            'fr': 'Géorgie du Sud et Îles Sandwich du Sud',
            'it': 'Isole Georgia del Sud e Sandwich del Sud',
            'en': 'South Georgia and the South Sandwich Islands',
        }
    },
    'GT': {
        'bfs_code': '8415',
        'iso3': 'GTM',
        'names': {
            'de': 'Guatemala',
            'fr': 'Guatemala',
            'it': 'Guatemala',
            'en': 'Guatemala',
        }
    },
    'GU': {
        'bfs_code': '8632',
        'iso3': 'GUM',
        'names': {
            'de': 'Guam',
            'fr': 'Guam',
            'it': 'Guam',
            'en': 'Guam',
        }
    },
    'GW': {
        'bfs_code': '8314',
        'iso3': 'GNB',
        'names': {
            'de': 'Guinea-Bissau',
            'fr': 'Guinée-Bissau',
            'it': 'Guinea-Bissau',
            'en': 'Guinea-Bissau',
        }
    },
    'GY': {
        'bfs_code': '8417',
        'iso3': 'GUY',
        'names': {
            'de': 'Guyana',
            'fr': 'Guyana',
            'it': 'Guyana',
            'en': 'Guyana',
        }
    },
    'HK': {
        'bfs_code': '8509',
        'iso3': 'HKG',
        'names': {
            'de': 'Hongkong',
            'fr': 'Hong Kong',
            'it': 'Hong Kong',
            'en': 'Hong Kong',
        }
    },
    'HM': {
        'bfs_code': '8653',
        'iso3': 'HMD',
        'names': {
            'de': 'Heard und McDonaldinseln',
            'fr': 'Îles-Heard-et-McDonald',
            'it': 'Isole Heard e McDonald',
            'en': 'Heard Island and McDonald Islands',
        }
    },
    'HN': {
        'bfs_code': '8420',
        'iso3': 'HND',
        'names': {
            'de': 'Honduras',
            'fr': 'Honduras',
            'it': 'Honduras',
            'en': 'Honduras',
        }
    },
    'HR': {
        'bfs_code': '8250',
        'iso3': 'HRV',
        'names': {
            'de': 'Kroatien',
            'fr': 'Croatie',
            'it': 'Croazia',
            'en': 'Croatia',
        }
    },
    'HT': {
        'bfs_code': '8418',
        'iso3': 'HTI',
        'names': {
            'de': 'Haiti',
            'fr': 'Haïti',
            'it': 'Haiti',
            'en': 'Haiti',
        }
    },
    'HU': {
        'bfs_code': '8240',
        'iso3': 'HUN',
        'names': {
            'de': 'Ungarn',
            'fr': 'Hongrie',
            'it': 'Ungheria',
            'en': 'Hungary',
        }
    },
    'ID': {
        'bfs_code': '8511',
        'iso3': 'IDN',
        'names': {
            'de': 'Indonesien',
            'fr': 'Indonésie',
            'it': 'Indonesia',
            'en': 'Indonesia',
        }
    },
    'IE': {
        'bfs_code': '8216',
        'iso3': 'IRL',
        'names': {
            'de': 'Irland',
            'fr': 'Irlande',
            'it': 'Irlanda',
            'en': 'Ireland',
        }
    },
    'IL': {
        'bfs_code': '8514',
        'iso3': 'ISR',
        'names': {
            'de': 'Israel',
            'fr': 'Israël',
            'it': 'Israele',
            'en': 'Israel',
        }
    },
    'IM': {
        'bfs_code': '8225',
        'iso3': 'IMN',
        'names': {
            'de': 'Insel Man',
            'fr': 'Île de Man',
            'it': 'Isola di Man',
            'en': 'Isle of Man',
        }
    },
    'IN': {
        'bfs_code': '8510',
        'iso3': 'IND',
        'names': {
            'de': 'Indien',
            'fr': 'Inde',
            'it': 'India',
            'en': 'India',
        }
    },
    'IO': {
        'bfs_code': '8371',
        'iso3': 'IOT',
        'names': {
            'de': 'Britische Territorien im Indischen Ozean',
            'fr': 'Territoires britanniques dans l\'océan indien',
            'it': 'Territori britannici nell\'oceano indiano',
            'en': 'British Territories in the Indian Ocean',
        }
    },
    'IQ': {
        'bfs_code': '8512',
        'iso3': 'IRQ',
        'names': {
            'de': 'Irak',
            'fr': 'Irak',
            'it': 'Iraq',
            'en': 'Iraq',
        }
    },
    'IR': {
        'bfs_code': '8513',
        'iso3': 'IRN',
        'names': {
            'de': 'Iran',
            'fr': 'Iran',
            'it': 'Iran',
            'en': 'Iran',
        }
    },
    'IS': {
        'bfs_code': '8217',
        'iso3': 'ISL',
        'names': {
            'de': 'Island',
            'fr': 'Islande',
            'it': 'Islanda',
            'en': 'Iceland',
        }
    },
    'IT': {
        'bfs_code': '8218',
        'iso3': 'ITA',
        'names': {
            'de': 'Italien',
            'fr': 'Italie',
            'it': 'Italia',
            'en': 'Italy',
        }
    },
    'JE': {
        'bfs_code': '8271',
        'iso3': 'JEY',
        'names': {
            'de': 'Jersey',
            'fr': 'Jersey',
            'it': 'Jersey',
            'en': 'Jersey',
        }
    },
    'JM': {
        'bfs_code': '8421',
        'iso3': 'JAM',
        'names': {
            'de': 'Jamaika',
            'fr': 'Jamaïque',
            'it': 'Giamaica',
            'en': 'Jamaica',
        }
    },
    'JO': {
        'bfs_code': '8517',
        'iso3': 'JOR',
        'names': {
            'de': 'Jordanien',
            'fr': 'Jordanie',
            'it': 'Giordania',
            'en': 'Jordan',
        }
    },
    'JP': {
        'bfs_code': '8515',
        'iso3': 'JPN',
        'names': {
            'de': 'Japan',
            'fr': 'Japon',
            'it': 'Giappone',
            'en': 'Japan',
        }
    },
    'KE': {
        'bfs_code': '8320',
        'iso3': 'KEN',
        'names': {
            'de': 'Kenia',
            'fr': 'Kenya',
            'it': 'Kenia',
            'en': 'Kenya',
        }
    },
    'KG': {
        'bfs_code': '8564',
        'iso3': 'KGZ',
        'names': {
            'de': 'Kirgisistan',
            'fr': 'Kirghizistan',
            'it': 'Kirghizistan',
            'en': 'Kyrgyzstan',
        }
    },
    'KH': {
        'bfs_code': '8518',
        'iso3': 'KHM',
        'names': {
            'de': 'Kambodscha',
            'fr': 'Cambodge',
            'it': 'Cambogia',
            'en': 'Cambodia',
        }
    },
    'KI': {
        'bfs_code': '8616',
        'iso3': 'KIR',
        'names': {
            'de': 'Kiribati',
            'fr': 'Kiribati',
            'it': 'Kiribati',
            'en': 'Kiribati',
        }
    },
    'KM': {
        'bfs_code': '8321',
        'iso3': 'COM',
        'names': {
            'de': 'Komoren',
            'fr': 'Comores',
            'it': 'Comore',
            'en': 'Comoros',
        }
    },
    'KN': {
        'bfs_code': '8445',
        'iso3': 'KNA',
        'names': {
            'de': 'St. Kitts und Nevis',
            'fr': 'Saint-Kitts-et-Nevis',
            'it': 'Saint Kitts e Nevis',
            'en': 'Saint Kitts and Nevis',
        }
    },
    'KP': {
        'bfs_code': '8530',
        'iso3': 'PRK',
        'names': {
            'de': 'Korea (Nord-)',
            'fr': 'Corée (Nord)',
            'it': 'Corea (Nord)',
            'en': 'North Korea',
        }
    },
    'KR': {
        'bfs_code': '8539',
        'iso3': 'KOR',
        'names': {
            'de': 'Korea (Süd-)',
            'fr': 'Corée (Sud)',
            'it': 'Corea (Sud)',
            'en': 'South Korea',
        }
    },
    'KW': {
        'bfs_code': '8521',
        'iso3': 'KWT',
        'names': {
            'de': 'Kuwait',
            'fr': 'Koweït',
            'it': 'Kuwait',
            'en': 'Kuwait',
        }
    },
    'KY': {
        'bfs_code': '8473',
        'iso3': 'CYM',
        'names': {
            'de': 'Kaimaninseln',
            'fr': 'Îles Cayman',
            'it': 'Isole Cayman',
            'en': 'Cayman Islands',
        }
    },
    'KZ': {
        'bfs_code': '8563',
        'iso3': 'KAZ',
        'names': {
            'de': 'Kasachstan',
            'fr': 'Kazakhstan',
            'it': 'Kazakstan',
            'en': 'Kazakhstan',
        }
    },
    'LA': {
        'bfs_code': '8522',
        'iso3': 'LAO',
        'names': {
            'de': 'Laos',
            'fr': 'Laos',
            'it': 'Laos',
            'en': 'Laos',
        }
    },
    'LB': {
        'bfs_code': '8523',
        'iso3': 'LBN',
        'names': {
            'de': 'Libanon',
            'fr': 'Liban',
            'it': 'Libano',
            'en': 'Lebanon',
        }
    },
    'LC': {
        'bfs_code': '8443',
        'iso3': 'LCA',
        'names': {
            'de': 'St. Lucia',
            'fr': 'Sainte-Lucie',
            'it': 'Saint Lucia',
            'en': 'Saint Lucia',
        }
    },
    'LI': {
        'bfs_code': '8222',
        'iso3': 'LIE',
        'names': {
            'de': 'Liechtenstein',
            'fr': 'Liechtenstein',
            'it': 'Liechtenstein',
            'en': 'Liechtenstein',
        }
    },
    'LK': {
        'bfs_code': '8506',
        'iso3': 'LKA',
        'names': {
            'de': 'Sri Lanka',
            'fr': 'Sri Lanka',
            'it': 'Sri Lanka',
            'en': 'Sri Lanka',
        }
    },
    'LR': {
        'bfs_code': '8325',
        'iso3': 'LBR',
        'names': {
            'de': 'Liberia',
            'fr': 'Libéria',
            'it': 'Liberia',
            'en': 'Liberia',
        }
    },
    'LS': {
        'bfs_code': '8324',
        'iso3': 'LSO',
        'names': {
            'de': 'Lesotho',
            'fr': 'Lesotho',
            'it': 'Lesotho',
            'en': 'Lesotho',
        }
    },
    'LT': {
        'bfs_code': '8262',
        'iso3': 'LTU',
        'names': {
            'de': 'Litauen',
            'fr': 'Lituanie',
            'it': 'Lituania',
            'en': 'Lithuania',
        }
    },
    'LU': {
        'bfs_code': '8223',
        'iso3': 'LUX',
        'names': {
            'de': 'Luxemburg',
            'fr': 'Luxembourg',
            'it': 'Lussemburgo',
            'en': 'Luxembourg',
        }
    },
    'LV': {
        'bfs_code': '8261',
        'iso3': 'LVA',
        'names': {
            'de': 'Lettland',
            'fr': 'Lettonie',
            'it': 'Lettonia',
            'en': 'Latvia',
        }
    },
    'LY': {
        'bfs_code': '8326',
        'iso3': 'LBY',
        'names': {
            'de': 'Libyen',
            'fr': 'Libye',
            'it': 'Libia',
            'en': 'Libya',
        }
    },
    'MA': {
        'bfs_code': '8331',
        'iso3': 'MAR',
        'names': {
            'de': 'Marokko',
            'fr': 'Maroc',
            'it': 'Marocco',
            'en': 'Morocco',
        }
    },
    'MC': {
        'bfs_code': '8226',
        'iso3': 'MCO',
        'names': {
            'de': 'Monaco',
            'fr': 'Monaco',
            'it': 'Monaco',
            'en': 'Monaco',
        }
    },
    'MD': {
        'bfs_code': '8263',
        'iso3': 'MDA',
        'names': {
            'de': 'Moldova',
            'fr': 'Moldova',
            'it': 'Moldova',
            'en': 'Moldova',
        }
    },
    'ME': {
        'bfs_code': '8254',
        'iso3': 'MNE',
        'names': {
            'de': 'Montenegro',
            'fr': 'Monténégro',
            'it': 'Montenegro',
            'en': 'Montenegro',
        }
    },
    'MF': {
        'bfs_code': '8448',
        'iso3': 'MAF',
        'names': {
            'de': 'Saint-Martin (Frankreich)',
            'fr': 'Saint-Martin (France)',
            'it': 'Saint-Martin (Francia)',
            'en': 'Saint Martin (France)',
        }
    },
    'MG': {
        'bfs_code': '8327',
        'iso3': 'MDG',
        'names': {
            'de': 'Madagaskar',
            'fr': 'Madagascar',
            'it': 'Madagascar',
            'en': 'Madagascar',
        }
    },
    'MH': {
        'bfs_code': '8617',
        'iso3': 'MHL',
        'names': {
            'de': 'Marshallinseln',
            'fr': 'Îles Marshall',
            'it': 'Isole Marshall',
            'en': 'Marshall Islands',
        }
    },
    'MK': {
        'bfs_code': '8255',
        'iso3': 'MKD',
        'names': {
            'de': 'Mazedonien',
            'fr': 'Macédoine',
            'it': 'Macedonia',
            'en': 'Macedonia',
        }
    },
    'ML': {
        'bfs_code': '8330',
        'iso3': 'MLI',
        'names': {
            'de': 'Mali',
            'fr': 'Mali',
            'it': 'Mali',
            'en': 'Mali',
        }
    },
    'MM': {
        'bfs_code': '8505',
        'iso3': 'MMR',
        'names': {
            'de': 'Myanmar',
            'fr': 'Myanmar',
            'it': 'Myanmar',
            'en': 'Myanmar',
        }
    },
    'MN': {
        'bfs_code': '8528',
        'iso3': 'MNG',
        'names': {
            'de': 'Mongolei',
            'fr': 'Mongolie',
            'it': 'Mongolia',
            'en': 'Mongolia',
        }
    },
    'MO': {
        'bfs_code': '8524',
        'iso3': 'MAC',
        'names': {
            'de': 'Macao',
            'fr': 'Macao',
            'it': 'Macao',
            'en': 'Macao',
        }
    },
    'MP': {
        'bfs_code': '8630',
        'iso3': 'MNP',
        'names': {
            'de': 'Nördliche Marianen',
            'fr': 'Mariannes du Nord',
            'it': 'Marianne del Nord',
            'en': 'Northern Marianas',
        }
    },
    'MQ': {
        'bfs_code': '8426',
        'iso3': 'MTQ',
        'names': {
            'de': 'Martinique',
            'fr': 'Martinique',
            'it': 'Martinica',
            'en': 'Martinique',
        }
    },
    'MR': {
        'bfs_code': '8332',
        'iso3': 'MRT',
        'names': {
            'de': 'Mauretanien',
            'fr': 'Mauritanie',
            'it': 'Mauritania',
            'en': 'Mauritania',
        }
    },
    'MS': {
        'bfs_code': '8475',
        'iso3': 'MSR',
        'names': {
            'de': 'Montserrat',
            'fr': 'Montserrat',
            'it': 'Monserrat',
            'en': 'Montserrat',
        }
    },
    'MT': {
        'bfs_code': '8224',
        'iso3': 'MLT',
        'names': {
            'de': 'Malta',
            'fr': 'Malte',
            'it': 'Malta',
            'en': 'Malta',
        }
    },
    'MU': {
        'bfs_code': '8333',
        'iso3': 'MUS',
        'names': {
            'de': 'Mauritius',
            'fr': 'Maurice',
            'it': 'Maurizio',
            'en': 'Mauritius',
        }
    },
    'MV': {
        'bfs_code': '8526',
        'iso3': 'MDV',
        'names': {
            'de': 'Malediven',
            'fr': 'Maldives',
            'it': 'Maldive',
            'en': 'Maldives',
        }
    },
    'MW': {
        'bfs_code': '8329',
        'iso3': 'MWI',
        'names': {
            'de': 'Malawi',
            'fr': 'Malawi',
            'it': 'Malawi',
            'en': 'Malawi',
        }
    },
    'MX': {
        'bfs_code': '8427',
        'iso3': 'MEX',
        'names': {
            'de': 'Mexiko',
            'fr': 'Mexique',
            'it': 'Messico',
            'en': 'Mexico',
        }
    },
    'MY': {
        'bfs_code': '8525',
        'iso3': 'MYS',
        'names': {
            'de': 'Malaysia',
            'fr': 'Malaisie',
            'it': 'Malaysia',
            'en': 'Malaysia',
        }
    },
    'MZ': {
        'bfs_code': '8334',
        'iso3': 'MOZ',
        'names': {
            'de': 'Mosambik',
            'fr': 'Mozambique',
            'it': 'Mozambico',
            'en': 'Mozambique',
        }
    },
    'NA': {
        'bfs_code': '8351',
        'iso3': 'NAM',
        'names': {
            'de': 'Namibia',
            'fr': 'Namibie',
            'it': 'Namibia',
            'en': 'Namibia',
        }
    },
    'NC': {
        'bfs_code': '8606',
        'iso3': 'NCL',
        'names': {
            'de': 'Neukaledonien',
            'fr': 'Nouvelle-Calédonie',
            'it': 'Nuova Caledonia',
            'en': 'New Caledonia',
        }
    },
    'NE': {
        'bfs_code': '8335',
        'iso3': 'NER',
        'names': {
            'de': 'Niger',
            'fr': 'Niger',
            'it': 'Niger',
            'en': 'Niger',
        }
    },
    'NF': {
        'bfs_code': '8654',
        'iso3': 'NFK',
        'names': {
            'de': 'Norfolkinsel',
            'fr': 'Île Norfolk',
            'it': 'Isola Norfolk',
            'en': 'Norfolk Island',
        }
    },
    'NG': {
        'bfs_code': '8336',
        'iso3': 'NGA',
        'names': {
            'de': 'Nigeria',
            'fr': 'Nigéria',
            'it': 'Nigeria',
            'en': 'Nigeria',
        }
    },
    'NI': {
        'bfs_code': '8429',
        'iso3': 'NIC',
        'names': {
            'de': 'Nicaragua',
            'fr': 'Nicaragua',
            'it': 'Nicaragua',
            'en': 'Nicaragua',
        }
    },
    'NL': {
        'bfs_code': '8227',
        'iso3': 'NLD',
        'names': {
            'de': 'Niederlande',
            'fr': 'Pays-Bas',
            'it': 'Paesi Bassi',
            'en': 'Netherlands',
        }
    },
    'NO': {
        'bfs_code': '8228',
        'iso3': 'NOR',
        'names': {
            'de': 'Norwegen',
            'fr': 'Norvège',
            'it': 'Norvegia',
            'en': 'Norway',
        }
    },
    'NP': {
        'bfs_code': '8529',
        'iso3': 'NPL',
        'names': {
            'de': 'Nepal',
            'fr': 'Népal',
            'it': 'Nepal',
            'en': 'Nepal',
        }
    },
    'NR': {
        'bfs_code': '8604',
        'iso3': 'NRU',
        'names': {
            'de': 'Nauru',
            'fr': 'Nauru',
            'it': 'Nauru',
            'en': 'Nauru',
        }
    },
    'NU': {
        'bfs_code': '8683',
        'iso3': 'NIU',
        'names': {
            'de': 'Niue',
            'fr': 'Nioué',
            'it': 'Niue',
            'en': 'Niue',
        }
    },
    'NZ': {
        'bfs_code': '8607',
        'iso3': 'NZL',
        'names': {
            'de': 'Neuseeland',
            'fr': 'Nouvelle-Zélande',
            'it': 'Nuova Zelanda',
            'en': 'New Zealand',
        }
    },
    'OM': {
        'bfs_code': '8527',
        'iso3': 'OMN',
        'names': {
            'de': 'Oman',
            'fr': 'Oman',
            'it': 'Oman',
            'en': 'Oman',
        }
    },
    'PA': {
        'bfs_code': '8430',
        'iso3': 'PAN',
        'names': {
            'de': 'Panama',
            'fr': 'Panama',
            'it': 'Panama',
            'en': 'Panama',
        }
    },
    'PE': {
        'bfs_code': '8432',
        'iso3': 'PER',
        'names': {
            'de': 'Peru',
            'fr': 'Pérou',
            'it': 'Perù',
            'en': 'Peru',
        }
    },
    'PF': {
        'bfs_code': '8671',
        'iso3': 'PYF',
        'names': {
            'de': 'Französisch-Polynesien',
            'fr': 'Polynésie française',
            'it': 'Polinesia francese',
            'en': 'French Polynesia',
        }
    },
    'PG': {
        'bfs_code': '8608',
        'iso3': 'PNG',
        'names': {
            'de': 'Papua-Neuguinea',
            'fr': 'Papouasie-Nouvelle-Guinée',
            'it': 'Papua Nuova Guinea',
            'en': 'Papua New Guinea',
        }
    },
    'PH': {
        'bfs_code': '8534',
        'iso3': 'PHL',
        'names': {
            'de': 'Philippinen',
            'fr': 'Philippines',
            'it': 'Filippine',
            'en': 'Philippines',
        }
    },
    'PK': {
        'bfs_code': '8533',
        'iso3': 'PAK',
        'names': {
            'de': 'Pakistan',
            'fr': 'Pakistan',
            'it': 'Pakistan',
            'en': 'Pakistan',
        }
    },
    'PL': {
        'bfs_code': '8230',
        'iso3': 'POL',
        'names': {
            'de': 'Polen',
            'fr': 'Pologne',
            'it': 'Polonia',
            'en': 'Poland',
        }
    },
    'PM': {
        'bfs_code': '8434',
        'iso3': 'SPM',
        'names': {
            'de': 'St. Pierre und Miquelon',
            'fr': 'Saint-Pierre-et-Miquelon',
            'it': 'Saint-Pierre e Miquelon',
            'en': 'Saint Pierre and Miquelon',
        }
    },
    'PN': {
        'bfs_code': '8685',
        'iso3': 'PCN',
        'names': {
            'de': 'Pitcairninseln',
            'fr': 'Îles Pitcairn',
            'it': 'Isole Pitcairn',
            'en': 'Pitcairn Islands',
        }
    },
    'PR': {
        'bfs_code': '8433',
        'iso3': 'PRI',
        'names': {
            'de': 'Puerto Rico',
            'fr': 'Porto Rico',
            'it': 'Portorico',
            'en': 'Puerto Rico',
        }
    },
    'PS': {
        'bfs_code': '8550',
        'iso3': 'PSE',
        'names': {
            'de': 'Palästina',
            'fr': 'Palestine',
            'it': 'Palestina',
            'en': 'Palestine',
        }
    },
    'PT': {
        'bfs_code': '8231',
        'iso3': 'PRT',
        'names': {
            'de': 'Portugal',
            'fr': 'Portugal',
            'it': 'Portogallo',
            'en': 'Portugal',
        }
    },
    'PW': {
        'bfs_code': '8619',
        'iso3': 'PLW',
        'names': {
            'de': 'Palau',
            'fr': 'Palaos',
            'it': 'Palau',
            'en': 'Palau',
        }
    },
    'PY': {
        'bfs_code': '8431',
        'iso3': 'PRY',
        'names': {
            'de': 'Paraguay',
            'fr': 'Paraguay',
            'it': 'Paraguay',
            'en': 'Paraguay',
        }
    },
    'QA': {
        'bfs_code': '8519',
        'iso3': 'QAT',
        'names': {
            'de': 'Katar',
            'fr': 'Qatar',
            'it': 'Qatar',
            'en': 'Qatar',
        }
    },
    'RE': {
        'bfs_code': '8339',
        'iso3': 'REU',
        'names': {
            'de': 'Reunion',
            'fr': 'Réunion',
            'it': 'Riunione',
            'en': 'Réunion',
        }
    },
    'RO': {
        'bfs_code': '8232',
        'iso3': 'ROU',
        'names': {
            'de': 'Rumänien',
            'fr': 'Roumanie',
            'it': 'Romania',
            'en': 'Romania',
        }
    },
    'RS': {
        'bfs_code': '8248',
        'iso3': 'SRB',
        'names': {
            'de': 'Serbien',
            'fr': 'Serbie',
            'it': 'Serbia',
            'en': 'Serbia',
        }
    },
    'RU': {
        'bfs_code': '8264',
        'iso3': 'RUS',
        'names': {
            'de': 'Russland',
            'fr': 'Russie',
            'it': 'Russia',
            'en': 'Russia',
        }
    },
    'RW': {
        'bfs_code': '8341',
        'iso3': 'RWA',
        'names': {
            'de': 'Ruanda',
            'fr': 'Rwanda',
            'it': 'Ruanda',
            'en': 'Rwanda',
        }
    },
    'SA': {
        'bfs_code': '8535',
        'iso3': 'SAU',
        'names': {
            'de': 'Saudi-Arabien',
            'fr': 'Arabie saoudite',
            'it': 'Arabia Saudita',
            'en': 'Saudi Arabia',
        }
    },
    'SB': {
        'bfs_code': '8614',
        'iso3': 'SLB',
        'names': {
            'de': 'Salomoninseln',
            'fr': 'Îles Salomon',
            'it': 'Isole Salomone',
            'en': 'Solomon Islands',
        }
    },
    'SC': {
        'bfs_code': '8346',
        'iso3': 'SYC',
        'names': {
            'de': 'Seychellen',
            'fr': 'Seychelles',
            'it': 'Seicelle',
            'en': 'Seychelles',
        }
    },
    'SD': {
        'bfs_code': '8350',
        'iso3': 'SDN',
        'names': {
            'de': 'Sudan',
            'fr': 'Soudan',
            'it': 'Sudan',
            'en': 'Sudan',
        }
    },
    'SE': {
        'bfs_code': '8234',
        'iso3': 'SWE',
        'names': {
            'de': 'Schweden',
            'fr': 'Suède',
            'it': 'Svezia',
            'en': 'Sweden',
        }
    },
    'SG': {
        'bfs_code': '8537',
        'iso3': 'SGP',
        'names': {
            'de': 'Singapur',
            'fr': 'Singapour',
            'it': 'Singapore',
            'en': 'Singapore',
        }
    },
    'SH': {
        'bfs_code': '8375',
        'iso3': 'SHN',
        'names': {
            'de': 'Tristan da Cunha',
            'fr': 'Tristan da Cunha',
            'it': 'Tristan da Cunha',
            'en': 'Tristan da Cunha',
        }
    },
    'SI': {
        'bfs_code': '8251',
        'iso3': 'SVN',
        'names': {
            'de': 'Slowenien',
            'fr': 'Slovénie',
            'it': 'Slovenia',
            'en': 'Slovenia',
        }
    },
    'SJ': {
        'bfs_code': '8273',
        'iso3': 'SJM',
        'names': {
            'de': 'Svalbard und Jan Mayen',
            'fr': 'Svalbard et Île Jan Mayen',
            'it': 'Svalbard e Jan Mayen',
            'en': 'Svalbard and Jan Mayen',
        }
    },
    'SK': {
        'bfs_code': '8243',
        'iso3': 'SVK',
        'names': {
            'de': 'Slowakei',
            'fr': 'Slovaquie',
            'it': 'Slovacchia',
            'en': 'Slovakia',
        }
    },
    'SL': {
        'bfs_code': '8347',
        'iso3': 'SLE',
        'names': {
            'de': 'Sierra Leone',
            'fr': 'Sierra Leone',
            'it': 'Sierra Leone',
            'en': 'Sierra Leone',
        }
    },
    'SM': {
        'bfs_code': '8233',
        'iso3': 'SMR',
        'names': {
            'de': 'San Marino',
            'fr': 'Saint-Marin',
            'it': 'San Marino',
            'en': 'San Marino',
        }
    },
    'SN': {
        'bfs_code': '8345',
        'iso3': 'SEN',
        'names': {
            'de': 'Senegal',
            'fr': 'Sénégal',
            'it': 'Senegal',
            'en': 'Senegal',
        }
    },
    'SO': {
        'bfs_code': '8348',
        'iso3': 'SOM',
        'names': {
            'de': 'Somalia',
            'fr': 'Somalie',
            'it': 'Somalia',
            'en': 'Somalia',
        }
    },
    'SR': {
        'bfs_code': '8435',
        'iso3': 'SUR',
        'names': {
            'de': 'Suriname',
            'fr': 'Suriname',
            'it': 'Suriname',
            'en': 'Suriname',
        }
    },
    'SS': {
        'bfs_code': '8363',
        'iso3': 'SSD',
        'names': {
            'de': 'Südsudan',
            'fr': 'Soudan du Sud',
            'it': 'Sudan del Sud',
            'en': 'South Sudan',
        }
    },
    'ST': {
        'bfs_code': '8344',
        'iso3': 'STP',
        'names': {
            'de': 'São Tomé und Príncipe',
            'fr': 'Sao Tomé-et-Principe',
            'it': 'São Tomé e Príncipe',
            'en': 'São Tomé and Príncipe',
        }
    },
    'SV': {
        'bfs_code': '8411',
        'iso3': 'SLV',
        'names': {
            'de': 'El Salvador',
            'fr': 'El Salvador',
            'it': 'El Salvador',
            'en': 'El Salvador',
        }
    },
    'SX': {
        'bfs_code': '8485',
        'iso3': 'SXM',
        'names': {
            'de': 'Sint Maarten (Niederlande)',
            'fr': 'Sint Maarten (Pays-Bas)',
            'it': 'Sint Maarten (Paesi Bassi)',
            'en': 'Sint Maarten (Netherlands)',
        }
    },
    'SY': {
        'bfs_code': '8541',
        'iso3': 'SYR',
        'names': {
            'de': 'Syrien',
            'fr': 'Syrie',
            'it': 'Siria',
            'en': 'Syria',
        }
    },
    'SZ': {
        'bfs_code': '8352',
        'iso3': 'SWZ',
        'names': {
            'de': 'Swasiland',
            'fr': 'Swaziland',
            'it': 'Swaziland',
            'en': 'Swaziland',
        }
    },
    'TC': {
        'bfs_code': '8474',
        'iso3': 'TCA',
        'names': {
            'de': 'Turks- und Caicosinseln',
            'fr': 'Îles Turques et Caïques',
            'it': 'Isole Turks e Caicos',
            'en': 'Turks and Caicos Islands',
        }
    },
    'TD': {
        'bfs_code': '8356',
        'iso3': 'TCD',
        'names': {
            'de': 'Tschad',
            'fr': 'Tchad',
            'it': 'Ciad',
            'en': 'Chad',
        }
    },
    'TF': {
        'bfs_code': '8703',
        'iso3': 'ATF',
        'names': {
            'de': 'Französische Süd- und Antarktisgebiete',
            'fr': 'Terres australes et antarctiques françaises',
            'it': 'Territori delle terre australi e antartiche francesi',
            'en': 'French Southern and Antarctic Lands',
        }
    },
    'TG': {
        'bfs_code': '8354',
        'iso3': 'TGO',
        'names': {
            'de': 'Togo',
            'fr': 'Togo',
            'it': 'Togo',
            'en': 'Togo',
        }
    },
    'TH': {
        'bfs_code': '8542',
        'iso3': 'THA',
        'names': {
            'de': 'Thailand',
            'fr': 'Thaïlande',
            'it': 'Thailandia',
            'en': 'Thailand',
        }
    },
    'TJ': {
        'bfs_code': '8565',
        'iso3': 'TJK',
        'names': {
            'de': 'Tadschikistan',
            'fr': 'Tadjikistan',
            'it': 'Tagikistan',
            'en': 'Tajikistan',
        }
    },
    'TK': {
        'bfs_code': '8684',
        'iso3': 'TKL',
        'names': {
            'de': 'Tokelau',
            'fr': 'Tokélau',
            'it': 'Tokelau',
            'en': 'Tokelau',
        }
    },
    'TL': {
        'bfs_code': '8547',
        'iso3': 'TLS',
        'names': {
            'de': 'Timor-Leste',
            'fr': 'Timor-Leste',
            'it': 'Timor-Leste',
            'en': 'Timor-Leste',
        }
    },
    'TM': {
        'bfs_code': '8566',
        'iso3': 'TKM',
        'names': {
            'de': 'Turkmenistan',
            'fr': 'Turkménistan',
            'it': 'Turkmenistan',
            'en': 'Turkmenistan',
        }
    },
    'TN': {
        'bfs_code': '8357',
        'iso3': 'TUN',
        'names': {
            'de': 'Tunesien',
            'fr': 'Tunisie',
            'it': 'Tunisia',
            'en': 'Tunisia',
        }
    },
    'TO': {
        'bfs_code': '8610',
        'iso3': 'TON',
        'names': {
            'de': 'Tonga',
            'fr': 'Tonga',
            'it': 'Tonga',
            'en': 'Tonga',
        }
    },
    'TR': {
        'bfs_code': '8239',
        'iso3': 'TUR',
        'names': {
            'de': 'Türkei',
            'fr': 'Turquie',
            'it': 'Turchia',
            'en': 'Turkey',
        }
    },
    'TT': {
        'bfs_code': '8436',
        'iso3': 'TTO',
        'names': {
            'de': 'Trinidad und Tobago',
            'fr': 'Trinité-et-Tobago',
            'it': 'Trinidad e Tobago',
            'en': 'Trinidad and Tobago',
        }
    },
    'TV': {
        'bfs_code': '8615',
        'iso3': 'TUV',
        'names': {
            'de': 'Tuvalu',
            'fr': 'Tuvalu',
            'it': 'Tuvalu',
            'en': 'Tuvalu',
        }
    },
    'TW': {
        'bfs_code': '8507',
        'iso3': 'TWN',
        'names': {
            'de': 'Taiwan (Chinesisches Taipei)',
            'fr': 'Taïwan (Taipei chinois)',
            'it': 'Taiwan (Taipei cinese)',
            'en': 'Taiwan (Chinese Taipei)',
        }
    },
    'TZ': {
        'bfs_code': '8353',
        'iso3': 'TZA',
        'names': {
            'de': 'Tansania',
            'fr': 'Tanzanie',
            'it': 'Tanzania',
            'en': 'Tanzania',
        }
    },
    'UA': {
        'bfs_code': '8265',
        'iso3': 'UKR',
        'names': {
            'de': 'Ukraine',
            'fr': 'Ukraine',
            'it': 'Ucraina',
            'en': 'Ukraine',
        }
    },
    'UG': {
        'bfs_code': '8358',
        'iso3': 'UGA',
        'names': {
            'de': 'Uganda',
            'fr': 'Ouganda',
            'it': 'Uganda',
            'en': 'Uganda',
        }
    },
    'UM': {
        'bfs_code': '8636',
        'iso3': 'UMI',
        'names': {
            'de': 'Wakeinsel',
            'fr': 'Île Wake',
            'it': 'Isola Wake',
            'en': 'Wake Island',
        }
    },
    'US': {
        'bfs_code': '8439',
        'iso3': 'USA',
        'names': {
            'de': 'Vereinigte Staaten',
            'fr': 'États-Unis',
            'it': 'Stati Uniti',
            'en': 'United States',
        }
    },
    'UY': {
        'bfs_code': '8437',
        'iso3': 'URY',
        'names': {
            'de': 'Uruguay',
            'fr': 'Uruguay',
            'it': 'Uruguay',
            'en': 'Uruguay',
        }
    },
    'UZ': {
        'bfs_code': '8567',
        'iso3': 'UZB',
        'names': {
            'de': 'Usbekistan',
            'fr': 'Ouzbékistan',
            'it': 'Uzbekistan',
            'en': 'Uzbekistan',
        }
    },
    'VA': {
        'bfs_code': '8241',
        'iso3': 'VAT',
        'names': {
            'de': 'Vatikanstadt',
            'fr': 'Cité du Vatican',
            'it': 'Città del Vaticano',
            'en': 'Vatican City',
        }
    },
    'VC': {
        'bfs_code': '8444',
        'iso3': 'VCT',
        'names': {
            'de': 'St. Vincent und die Grenadinen',
            'fr': 'Saint-Vincent-et-les Grenadines',
            'it': 'Saint Vincent e Grenadine',
            'en': 'Saint Vincent and the Grenadines',
        }
    },
    'VE': {
        'bfs_code': '8438',
        'iso3': 'VEN',
        'names': {
            'de': 'Venezuela',
            'fr': 'Venezuela',
            'it': 'Venezuela',
            'en': 'Venezuela',
        }
    },
    'VG': {
        'bfs_code': '8476',
        'iso3': 'VGB',
        'names': {
            'de': 'Jungferninseln (UK)',
            'fr': 'Îles Vierges britanniques',
            'it': 'Isole Vergini britanniche',
            'en': 'British Virgin Islands',
        }
    },
    'VI': {
        'bfs_code': '8472',
        'iso3': 'VIR',
        'names': {
            'de': 'Jungferninseln (USA)',
            'fr': 'Îles Vierges américaines',
            'it': 'Isole Vergini americane',
            'en': 'US Virgin Islands',
        }
    },
    'VN': {
        'bfs_code': '8545',
        'iso3': 'VNM',
        'names': {
            'de': 'Vietnam',
            'fr': 'Vietnam',
            'it': 'Vietnam',
            'en': 'Vietnam',
        }
    },
    'VU': {
        'bfs_code': '8605',
        'iso3': 'VUT',
        'names': {
            'de': 'Vanuatu',
            'fr': 'Vanuatu',
            'it': 'Vanuatu',
            'en': 'Vanuatu',
        }
    },
    'WF': {
        'bfs_code': '8611',
        'iso3': 'WLF',
        'names': {
            'de': 'Wallis und Futuna',
            'fr': 'Wallis-et-Futuna',
            'it': 'Wallis e Futuna',
            'en': 'Wallis and Futuna',
        }
    },
    'WS': {
        'bfs_code': '8612',
        'iso3': 'WSM',
        'names': {
            'de': 'Samoa',
            'fr': 'Samoa',
            'it': 'Samoa',
            'en': 'Samoa',
        }
    },
    'YE': {
        'bfs_code': '8516',
        'iso3': 'YEM',
        'names': {
            'de': 'Jemen',
            'fr': 'Yémen',
            'it': 'Yemen',
            'en': 'Yemen',
        }
    },
    'YT': {
        'bfs_code': '8361',
        'iso3': 'MYT',
        'names': {
            'de': 'Mayotte',
            'fr': 'Mayotte',
            'it': 'Mayotte',
            'en': 'Mayotte',
        }
    },
    'ZA': {
        'bfs_code': '8349',
        'iso3': 'ZAF',
        'names': {
            'de': 'Südafrika',
            'fr': 'Afrique du Sud',
            'it': 'Sudafrica',
            'en': 'South Africa',
        }
    },
    'ZM': {
        'bfs_code': '8343',
        'iso3': 'ZMB',
        'names': {
            'de': 'Sambia',
            'fr': 'Zambie',
            'it': 'Zambia',
            'en': 'Zambia',
        }
    },
    'ZW': {
        'bfs_code': '8340',
        'iso3': 'ZWE',
        'names': {
            'de': 'Simbabwe',
            'fr': 'Zimbabwe',
            'it': 'Zimbabwe',
            'en': 'Zimbabwe',
        }
    },
}

# Type hints
from typing import Optional, Dict, Any

# Helper functions
def get_bfs_country_code(iso_code: str) -> Optional[str]:
    """Get BFS country code from ISO 2-letter code.

    Args:
        iso_code: ISO 3166-1 alpha-2 country code (e.g., 'CH', 'DE')

    Returns:
        BFS country code or None if not found
    """
    country = COUNTRY_CODES.get(iso_code.upper())
    return country['bfs_code'] if country else None


def get_country_name(iso_code: str, language: str = 'de') -> Optional[str]:
    """Get country name in specified language.

    Args:
        iso_code: ISO 3166-1 alpha-2 country code
        language: Language code ('de', 'fr', 'it', 'en')

    Returns:
        Country name or None if not found
    """
    country = COUNTRY_CODES.get(iso_code.upper())
    if country and language in country['names']:
        return country['names'][language]
    return None


def get_country_by_bfs_code(bfs_code: str) -> Optional[Dict[str, Any]]:
    """Get country data by BFS code.

    Args:
        bfs_code: BFS country code (e.g., '8207' for Switzerland)

    Returns:
        Country data dict or None if not found
    """
    bfs_str = str(bfs_code)
    for iso_code, data in COUNTRY_CODES.items():
        if data['bfs_code'] == bfs_str:
            return {'iso2': iso_code, **data}
    return None
