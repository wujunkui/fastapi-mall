import React from "react";
import Image from "next/image";
import Search from "antd/es/input/Search";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center bg-white">
      <Head></Head>
      <Search className="px-4 mt-2" placeholder="输入菜名搜索"></Search>
      <Body>
        <Item></Item>
      </Body>
    </main>
  );
}

const Head: React.FC = () => {
  return (
    <div>
      <div className="mt-2">今日菜价</div>
    </div>
  );
};

const Body: React.FC = ({ children }) => {
  return <div className="flex">{children}</div>;
};

const Foot: React.FC = () => {
  return <div></div>;
};

const Item: React.FC = () => {
  return (
    <div className="min-h-24 border">
      <span>土豆</span>
    </div>
  );
};
