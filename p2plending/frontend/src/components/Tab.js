import React from "react";
import cx from "classnames";

// eslint-disable-next-line react/prop-types
const Tab = ({ active, children, onClick }) => (
  <div
    onClick={onClick}
    className={cx("text-uppercase py-2 px-3", { "border-primary": active })}
    style={{ borderBottom: active ? "2px solid blue" : "none", cursor: "pointer" }}
  >
    <span
      className={cx("small font-weight-medium", {
        "text-primary": active,
        "text-muted": !active,
      })}
    >
      {children}
    </span>
  </div>
);

export default Tab;
