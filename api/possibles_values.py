# Ce fichier permet de definir les parametres attendus par l'api, celà rend l'api plus simple d'utilisation pour un néophyte et améliore l'UX

from enum import Enum


class Job_title(str, Enum):
    data_scientist = 'Data Scientist',
    data_engeering_manager = 'Data Engineering Manager',
    principal_data_scientist = 'Principal Data Scientist',
    data_analytics_engineer = 'Data Analytics Engineer',
    data_science_consultant = 'Data Science Consultant',
    machine_learning_engineer = 'Machine Learning Engineer',
    director_of_data_science = 'Director of Data Science',
    data_analyst = 'Data Analyst',
    data_engineer = 'Data Engineer',
    business_data_analyst = 'Business Data Analyst',
    bi_data_analyst = 'BI Data Analyst',
    big_data_engineer = 'Big Data Engineer',
    data_science_manager = 'Data Science Manager',
    head_of_data = 'Head of Data',
    machine_learning_scientist = 'Machine Learning Scientist',
    data_analytics_manager = 'Data Analytics Manager',
    data_architect = 'Data Architect',
    head_of_data_science = 'Head of Data Science',
    analytics_engieneer = 'Analytics Engineer',
    ai_scientist = 'AI Scientist',
    computer_vision_engieneer = 'Computer Vision Engineer',
    research_scientist = 'Research Scientist',
    applied_data_scientist = 'Applied Data Scientist',
    lead_data_engineer = 'Lead Data Engineer',


class Company_size(str, Enum):
    large = 'Large',
    small = 'Small',
    medium = 'Medium'


class Company_country_location(str, Enum):
    germany = 'Germany',
    usa = 'United States of America',
    uk = 'United Kingdom of Great Britain and Northern Ireland',
    canada = 'Canada',
    france = 'France',
    spain = 'Spain',
    india = 'India',
    greece = 'Greece'


class Experience_level(str, Enum):
    intermediate = 'Intermediate',
    senior = 'Senior',
    junior = 'Junior',
    expert = 'Expert'


class Employee_country_residence(str, Enum):
    germany = 'Germany',
    usa = 'United States of America',
    uk = 'United Kingdom of Great Britain and Northern Ireland',
    canada = 'Canada',
    france = 'France',
    spain = 'Spain',
    india = 'India',
    greece = 'Greece',
    pakistan = 'Pakistan',
    netherlands = 'Netherlands',
    brazil = 'Brazil',
    poland = 'Poland'


class Remote_ratio(str, Enum):
    data_scientist = '0',
    data_engeering_manager = '50',
    principal_data_scientist = '100',
