/**
 * Component Specification: ProjectCard
 * ----------------------------------------------------------------------------
 * A responsive, accessible, and reusable portfolio card designed for student projects.
 *
 * Expected Props:
 * - title (string, required): Title of the software project
 * - description (string, required): Short summary of project functionality
 * - image (string, optional): Preview screenshot or thumbnail image
 * - technologies (string[], optional): Array of technology tags (e.g. ['React', 'Vite', 'CSS3'])
 * - projectUrl (string, optional): Live demo or repository URL
 *
 * Fallback Handling:
 * - If `image` is missing, renders a styled placeholder banner.
 * - If `technologies` is empty, omits the tag row gracefully.
 * - If `projectUrl` is omitted, renders an inactive "Coming Soon" badge instead of a dead link.
 * ----------------------------------------------------------------------------
 */

import React from 'react';
import PropTypes from 'prop-types';

function ProjectCard({
  title,
  description,
  image,
  technologies = [],
  projectUrl,
}) {
  return (
    <article className="project-card">
      <div className="project-image-box">
        {image ? (
          <img src={image} alt={`Screenshot of ${title}`} className="project-thumb" />
        ) : (
          <div className="project-thumb-placeholder" aria-label="No preview image">
            <span>💻 Project Preview</span>
          </div>
        )}
      </div>

      <div className="project-body">
        <h3 className="project-title">{title}</h3>
        <p className="project-desc">{description}</p>

        {technologies && technologies.length > 0 && (
          <div className="tech-tags-row">
            {technologies.map((tech) => (
              <span key={tech} className="tech-tag">
                {tech}
              </span>
            ))}
          </div>
        )}

        <div className="project-actions">
          {projectUrl ? (
            <a
              href={projectUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="project-link-btn"
              aria-label={`View live project for ${title}`}
            >
              View Project ↗
            </a>
          ) : (
            <span className="coming-soon-pill">Internal Preview</span>
          )}
        </div>
      </div>
    </article>
  );
}

ProjectCard.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  image: PropTypes.string,
  technologies: PropTypes.arrayOf(PropTypes.string),
  projectUrl: PropTypes.string,
};

export default ProjectCard;

