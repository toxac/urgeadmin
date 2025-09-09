create view public.offerings_with_details as
select
  o.id as offering_id,
  o.name as offering_name,
  o.description as offering_description,
  o.base_price_amount,
  o.currency,
  o.duration_months,
  o.entity_type,
  o.related_entity_id,
  o.is_active,
  o.created_at as offering_created_at,
  o.updated_at as offering_updated_at,
  e.title as event_title,
  e.description as event_description,
  e.start_time as event_start_time,
  e.end_time as event_end_time,
  e.event_format,
  e.event_type,
  e.location,
  e.online_link,
  e.featured_image_url as event_image,
  e.capacity as event_capacity,
  e.is_member_only as event_member_only,
  e.exhibits as event_exhibits,
  e.sessions as event_sessions,
  e.created_by as event_created_by,
  p.name as program_name,
  p.description as program_description,
  p.mode as program_mode,
  p.type as program_type,
  p.created_at as program_created_at,
  p.updated_at as program_updated_at
from
  offerings o
  left join events e on o.entity_type = 'event'::text
  and o.related_entity_id = e.id
  left join programs p on o.entity_type = 'program'::text
  and o.related_entity_id = p.id;