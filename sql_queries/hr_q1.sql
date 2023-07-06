select
    concat(p.firstname,' ',p.lastname) as "Name",
    e.emailaddress,
    hr.jobtitle,
    hr.vacationhours
from
    person.person as p
join person.emailaddress as e on
    e.businessentityid = p.businessentityid
join humanresources.employee as hr on
    p.businessentityid = hr.businessentityid
where
    p.persontype in ('SP', 'EM')
    and hr.vacationhours >= 40;